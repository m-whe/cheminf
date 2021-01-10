# smiles-to-inchi-key.py
# Michael He
#
# Takes .csv file of ID, SMILES(canonical) as input
# Uses RDKit to convert canonical smiles to inchi_keys
# Writes .csv file of ID, SMILES, inchi_keys
#
# To use, update '{file_directory}' with local user read/write directory and '{file.csv}' with input filename
#
# Compatability: Linux
# Requirements: conda, rdkit
# For instructions on how to set up RDKit, visit: https://www.rdkit.org/docs/Install.html
#
# Launch RDKit environment with $ conda activate my-rdkit-env
#
# Sample input file of kinase inhibitors included as SMILES.csv

import rdkit
from rdkit import Chem

import csv


# UPDATE DIRECTORY VARIABLES HERE
input_file = '{file.csv}'
file_dir = '{file_directory}'

fi = file_dir + '/' + input_file
fi_out = file_dir + '/inchi_keys.csv' 

id_col = []
smiles_col = []
inchi_keys = []
column_names = []

with open(fi, newline='') as csvfile:
     SMILES = csv.reader(csvfile)
     for row in SMILES:
          id_col.append(row[0])
          smiles_col.append(row[1])

smiles2 = smiles_col[1:]

for i in smiles2:
     rdkit_mol = Chem.MolFromSmiles(i)
     inchi_key = Chem.MolToInchiKey(rdkit_mol)
     inchi_keys.append(inchi_key)

inchi_keys = ['inchi_key'] + inchi_keys

column_names = [id_col[0], inchi_keys[0]]
ids = id_col[1:]
keys = inchi_keys[1:]
length = len(keys)
i = 0

f = open(fi_out,'w+')
f.write(id_col[0] + ',' + smiles_col[0] + ',' + inchi_keys[0] + '\n')
while i < len(keys):
     f.write(ids[i] + ',' + smiles2[i] + ',' + keys[i] + '\n')
     i += 1
f.close()
