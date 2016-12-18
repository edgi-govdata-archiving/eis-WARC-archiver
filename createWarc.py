import subprocess
import csv
import os

#Input = subprocess.call(["wget", "--warc-file", "/Users/sonal/SideProjects/WarcCreator/my-warc-file.warc", "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details?eisId=219321"])

#path to the CSV with the unique IDs to each EIS
csv_Path = 'eis-listing.csv'

#base URL for the EIS page
base_HTML_EPA_url = 'https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details?eisId='

#base URL for each EIS Documents
base_Documents_EPA_url = 'https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details/downloadEisDocuments?eisId='

#base URL each EIS Letter comments
base_Letters_EPA_url = 'https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details/downloadCommentLetters?eisId='


with open(csv_Path) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        epaurl = base_HTML_EPA_url+row['eis_id']
        warcHTMLOutputPath = "WARC_OUTPUT/"+row['eis_id'] +"/HTML/"
        DocumentsOutputPath = "WARC_OUTPUT/"+row['eis_id'] + "/DOCUMENTS/"
        LettersOutputPath = "WARC_OUTPUT/"+row['eis_id'] + "/LETTERS/"
        if not os.path.exists(warcHTMLOutputPath):
            os.makedirs(warcHTMLOutputPath)
            os.makedirs(DocumentsOutputPath)
            os.makedirs(LettersOutputPath)
            html = subprocess.call(["wget", "--warc-file", warcHTMLOutputPath + row['eis_id'], epaurl + row['eis_id'], "--delete-after"])
            letterDocs = subprocess.call(["wget", base_Letters_EPA_url + row['eis_id'], "-O" + LettersOutputPath + row['eis_id'] + ".zip"])
            eisDocs = subprocess.call(["wget", base_Documents_EPA_url + row['eis_id'],"-O"+DocumentsOutputPath + row['eis_id'] + ".zip"])
