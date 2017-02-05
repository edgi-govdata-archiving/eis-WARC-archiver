import csv

csv_Path = 'eis-listing.csv'
base_HTML_EPA_url = 'https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details?eisId='

with open(csv_Path) as csvfile:
    reader = csv.DictReader(csvfile)
    text_file = open("EISIds.txt", "w")
    for row in reader:
        epaurl = 'eisId='+row['eis_id']
        text_file.write(epaurl + '\n')

text_file.close()