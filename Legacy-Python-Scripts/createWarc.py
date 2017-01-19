import subprocess
import csv
import os
import time

#Input = subprocess.call(["wget", "--warc-file", "/Users/sonal/SideProjects/WarcCreator/my-warc-file.warc", "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details?eisId=219321"])

#path to the CSV with the unique IDs to each EIS
csv_Path = 'eis-listing.csv'

#base URL for the EIS page
base_HTML_EPA_url = 'https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details?eisId='

#base URL for each EIS Documents
base_Documents_EPA_url = 'https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details/downloadEisDocuments?eisId='

#base URL each EIS Letter comments
base_Letters_EPA_url = 'https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details/downloadCommentLetters?eisId='

#loop through each row in the csv file and append the EIS unique id to each base URL to perform the wget calls
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
            #wget has a option flag to pacakge the response in WARC format, unfortunately when supplying multiple urls to one singl WARC, the documents are corrupted
            #therefore they are grabbed in 3 different wget calls
            subprocess.call(["wget", "--warc-file", warcHTMLOutputPath + row['eis_id'], epaurl + row['eis_id'], "--delete-after"])
            time.sleep(5)
            subprocess.call(["wget", base_Letters_EPA_url + row['eis_id'], "-O" + LettersOutputPath + row['eis_id'] + ".zip"])
            time.sleep(5)
            subprocess.call(["wget", base_Documents_EPA_url + row['eis_id'],"-O"+DocumentsOutputPath + row['eis_id'] + ".zip"])
            time.sleep(5)