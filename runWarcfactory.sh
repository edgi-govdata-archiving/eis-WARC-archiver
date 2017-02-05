#!/bin/bash

file=$1
lines=`cat $file`
for line in $lines; do
	echo "$line"
	docker exec warcfactory grab-site --no-offsite-links $line
done
