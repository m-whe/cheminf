# Takes .csv file of ID, SMILES(canonical) as input
# Uses RDKit to convert canonical smiles to inchi_keys
# Writes .csv file of ID, inchi_keys
#
# To use, update '{file_directory}' with local user read/write directory and '{file.csv}' with input filename
# Compatability: Linux
# Sample input file included as SMILES.csv

import rdkit
from rdkit import Chem

import csv

id_col = []
smiles_col = []
inchi_keys = []
column_names = []

with open('/{file_directory}/{file.csv}', newline='') as csvfile:
     SMILES = csv.reader(csvfile)
     for row in SMILES:
          id_col.append(row[0])
          smiles_col.append(row[1])

smiles_col.pop(0)

for i in smiles_col:
     rdkit_mol = Chem.MolFromSmiles(i)
     inchi_key = Chem.MolToInchiKey(rdkit_mol)
     inchi_keys.append(inchi_key)

inchi_keys = ['inchi_key'] + inchi_keys

column_names = [id_col[0], inchi_keys[0]]
col = id_col[1:]
keys = inchi_keys[1:]
length = len(keys)
i = 0

f = open('{file_directory}/inchi_keys.csv','w+')
f.write(id_col[0] + ',' + inchi_keys[0] + '\n')
while i < len(keys):
     f.write(col[i] + ',' + keys[i] + '\n')
     i += 1
f.close()
