import csv
import sys

#path to csv
csv_Path = sys.argv[1]

#Key from the CSV
key = sys.argv[2]

#Base url
baseURL = sys.argv[3]

with open(csv_Path) as csvfile:
    reader = csv.DictReader(csvfile)
    text_file = open("paths.txt", "w")
    for row in reader:
        fullURL =  baseURL+row[key]
        text_file.write(fullURL + '\n')

text_file.close()