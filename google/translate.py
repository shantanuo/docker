# coding: utf-8
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/tmp/passwd.json"

from google.cloud import translate
translate_client = translate.Client()

for (dirpath, dirnames, filenames) in os.walk('/tmp/ibps/'):
    for x in filenames:
        with open(dirpath.replace('ibps', 'ibps2')+x, 'w') as ot:
            with open(dirpath+'/'+x) as f:
                i=f.readlines()
                for n in i:
                    try:
                        text = n.split(':')[1]
                        result = translate_client.translate(text, target_language='mr')
                        ot.write('{} {} {}\n'.format(n.split(':')[0], ":", result['translatedText']))
                    except:
                        pass
