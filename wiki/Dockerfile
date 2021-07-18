FROM ubuntu
RUN apt update && apt --yes install libxml-xpath-perl wget unzip curl

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install

RUN wget 'https://mr.wikipedia.org/w/api.php?hidebots=1&hidecategorization=1&hideWikibase=1&urlversion=2&days=14&limit=50&action=feedrecentchanges&feedformat=atom' -O /tmp/out1.txt
 
RUN PERL5OPT=-CA xpath -e "/feed/entry[author/name!='Aditya tamhankar' and author/name!='Dharmadhyaksha' and author/name!='नरेश सावे' and author/name!='अभय नातू']" /tmp/out1.txt > /tmp/updated.txt

AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

aws s3 cp /tmp/out1.txt s3://abc/wiki/
