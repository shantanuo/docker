#!/bin/sh
wget 'https://mr.wikipedia.org/w/api.php?hidebots=1&hidecategorization=1&hideWikibase=1&urlversion=2&days=30&limit=500&action=feedrecentchanges&feedformat=atom' -O /tmp/out1.txt

head -9 /tmp/out1.txt > /tmp/updated.txt
PERL5OPT=-CA xpath -e "/feed/entry[author/name!='Aditya tamhankar' and author/name!='Dharmadhyaksha' and author/name!='नरेश सावे' and author/name!='अभय नातू' and author/name!='संतोष गोरे' and author/name!='Khirid Harshad'  and author/name!=Ganesh591' and author/name!='Abhijitsathe']" /tmp/out1.txt >> /tmp/updated.txt
tail -1 /tmp/out1.txt >> /tmp/updated.txt

aws s3 cp /tmp/updated.txt s3://gamabhana/wiki/ --acl public-read
