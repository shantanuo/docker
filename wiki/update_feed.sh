#!/bin/sh
wget 'https://mr.wikipedia.org/w/api.php?hidebots=1&hidecategorization=1&hideWikibase=1&urlversion=2&days=14&limit=50&action=feedrecentchanges&feedformat=atom' -O /tmp/out1.txt

PERL5OPT=-CA xpath -e "/feed/entry[author/name!='Aditya tamhankar' and author/name!='Dharmadhyaksha' and author/name!='नरेश सावे' and author/name!='अभय नातू']" /tmp/out1.txt > /tmp/updated.txt

aws s3 cp /tmp/updated.txt s3://abc/ --acl public-read
