# EIS Archiver
This is a python script that will parse through a giving csv with EIS ID's and use the wget function grab and package the EIS URL in a WARC format and download any documents associated with the EIS into a zip format.

The `wget` bash function has a option flag to package the response from the supplied URL into a `.warc` format which the Web ARCHive file format the Internet Archive uses to playback web sites.

The python script `createWarc.py` invokes a wget command as a subprocess in the script to package the response from the supplied URL into a warc format. The pdf links present in the html page cannot be preserved in the html therefore, they are being downloaded separately in a different wget call.

The EIS csv is supplied from this [parser](https://github.com/titaniumbones/eot-sprint-toolkit/tree/master/eis)
This script continues on the work done for the URL scraping list supplied by one of the groups from the Guerrilla Archiving Event taken place at University of Toronto on December 16, 2016.

## Dependecies
This script has only been tested on OSX and Linux environment. If you would like to contribute to support Windows please contribute.

1. wget function available in your bash shell
2. python 2.7

## Usage
Clone this repo then just simply run the python script `python createWarc.py`
Supplied is the csv, if you would like to customize this python or expand and modify the script to a take in generic datasets please modify the csv, base urls accordingly.

This script is specifically written for the Enivornment Impact Statement documents from the EPA [site](https://cdxnodengn.epa.gov/cdx-enepa-public/action/eis/search)
