file="EIS_URLs-Dec18.txt"
lines=`cat $file`
for line in $lines; do
	echo "$line"
	docker exec warcfactory grab-site --no-offsite-links $line
done
