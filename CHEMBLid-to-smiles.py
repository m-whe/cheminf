# CHEMBLid-to-smiles.py
# Michael He
#
# Takes ChEMBL ID as input
# Uses pycurl to send a GET request to query the ChEMBL API
# Writes .xml file of ChEMBL API query
# Parses .xml with BeautifulSoup, lxml
# Writes .csv file of ChEBML ID, SMILES
#
# To use, update '{file_directory}' with local output write directory and CHEMBLID_query with ChEMBL ID of interest
#
# Compatability: Linux
# Requirements: bs4, lxml, pycurl, certifi
#
# Sample CHEMBL ID included

import csv
import pycurl
import certifi
from io import BytesIO
from bs4 import BeautifulSoup as bs

CHEMBLID_query = 'CHEMBL163'
CHEMBL_url = 'https://www.ebi.ac.uk/chembl/api/data/molecule/search?q=' + CHEMBLID_query     #GET request
file_dir = '{file_directory}'
xml_dir = file_dir + '/CHEMBL_query.xml'
csv_dir = file_dir + '/CHEMBL_query.csv'

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, CHEMBL_url)
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.CAINFO, certifi.where())
c.setopt(c.VERBOSE, True)
c.perform()
c.close

body = buffer.getvalue()

with open(xml_dir, 'wb') as f:
     f.write(body)

with open(xml_dir, 'r') as file:
     content = file.readlines()
     content = ''.join(content)
     bs_content = bs(content, 'lxml')

result = str(bs_content.find('canonical_smiles'))
r1 = result.split('>')
r2 = r1[1]
r3 = r2.split('<')
smiles = r3[0]
col_names = 'CHEMBL_ID,SMILES'

f = open(csv_dir, 'w+')
f.write(col_names + '\n')
f.write(CHEMBLID_query + ',' + smiles + '\n')
f.close()
