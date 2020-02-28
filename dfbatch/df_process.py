# !git clone https://github.com/hitz02/Sentiment_Analysis_Phone_Review.git

import pandas as pd
import numpy as np
import random, re
import string
import os

import nltk
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")
nltk.download('averaged_perceptron_tagger')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

stop = set(stopwords.words("english"))

import warnings
warnings.filterwarnings("ignore")

import boto
from boto.s3.key import Key
from boto.s3.connection import OrdinaryCallingFormat

#!wget https://www.dropbox.com/s/v9uuv635lv1idjf/en_large.pkl.zip
#!unzip en_large.pkl.zip

from spello.model import SpellCorrectionModel

sp = SpellCorrectionModel(language="en")
sp.load("/tmp/en_large.pkl")

import pkg_resources
from symspellpy import SymSpell, Verbosity

sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt"
)

sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

df = pd.read_csv("K8 Reviews v0.2.csv")

slices = os.getenv("slices") or 10
index_value = os.getenv("index_value") or 1
bucketname = os.getenv("mybucket") or "todel162"
ac = os.getenv("ac") or "xxx"
se = os.getenv("se") or "xxx"

start = (int(index_value) - 1) * int(len(df) / int(slices))
end = int(index_value) * int(len(df) / int(slices))
end = end if end < len(df) else len(df)

df = df.iloc[start:end]

stemmer = PorterStemmer()
lemm = WordNetLemmatizer()

def tokenize(text):
    words = re.split(r"[^A-Za-z]", text)
    text = " ".join(words)
    text = sym_spell.word_segmentation(text)[0]
    try:
        corrected = sp.spell_correct(text)["spell_corrected_text"]
    except:
        corrected = text
    mylist = list()
    for word, tag in nltk.pos_tag(corrected.split()):
        wntag = tag[0].lower()
        wntag = wntag if wntag in ["a", "r", "n", "v"] else None
        lemma = lemm.lemmatize(word, wntag) if wntag else word
        mylist.append(lemma)
    return " ".join(mylist)


df["reviews"] = df.review.apply(tokenize)

filename = "/tmp/df" + index_value + ".csv"

df.to_csv(filename)

path = ""
s3_conn = boto.connect_s3(
    aws_access_key_id=ac,
    aws_secret_access_key=se,
    calling_format=OrdinaryCallingFormat(),
)
k = Key(bucketname)
key_name = filename.split("/")[-1]
full_key_name = os.path.join(path, key_name)
mybucket = s3_conn.get_bucket(bucketname)
k = mybucket.new_key(full_key_name)
k.set_contents_from_filename(filename)
