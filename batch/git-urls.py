import argparse
import feedparser
from bs4 import BeautifulSoup
import boto3

parser = argparse.ArgumentParser()
parser.add_argument("access")
parser.add_argument("secret")
parser.add_argument("region")
args = parser.parse_args()

myaccess = args.access
mysecret = args.secret
myregion = args.region

url = "https://towardsdatascience.com/feed"
feed = feedparser.parse(url)

dynamodb = boto3.resource('dynamodb',  aws_access_key_id=myaccess, aws_secret_access_key=mysecret,  region_name=myregion)
table = dynamodb.Table("Movies")

for post in feed.entries:
    soup = BeautifulSoup(post.description, features="html.parser")
    for link in soup.findAll("a"):
        if "http" in link.get("href"):
            response = table.put_item(Item={"title": link.get("href")})

"""
python test.py 'access_key_xxx' 'secret_key_xxx'  'us-east-1'
"""
