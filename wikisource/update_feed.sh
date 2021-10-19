#!/bin/sh
wget 'https://mr.wikisource.org/w/api.php?hidebots=1&hidecategorization=1&hideWikibase=1&urlversion=2&days=30&limit=500&action=feedrecentchanges&feedformat=atom' -O /tmp/out1.txt

head -9 /tmp/out1.txt > /tmp/updated_source.txt
PERL5OPT=-CA xpath -e "/feed/entry[author/name!='अश्विनीलेले' and author/name!='अरुणा केळकर.']" /tmp/out1.txt >> /tmp/updated_source.txt
tail -1 /tmp/out1.txt >> /tmp/updated_source.txt

aws s3 cp /tmp/updated_source.txt s3://gamabhana/wiki/ --acl public-read
