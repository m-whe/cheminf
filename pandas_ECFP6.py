# pandas_ECFP6.py
# Michael He
#
# Takes .csv file of ID, SMILES_canonical as input
# Uses pandas to load .csv as pandas dataframe
# Uses RDKit to generate ECFP6 Morgan Fingerprints
#
# To use, update '{filepath}' with local filepath
#
# Compatability: Linux
# Requirements: conda, rdkit, pandas
# For instructions on how to set up RDKit, visit: https://www.rdkit.org/docs/Install.html
#
# Launch RDKit environment with $ conda activate my-rdkit-env
#
# Sample input file of kinase inhibitors included as SMILES.csv

import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem

file = pd.read_csv('{filepath}')

mols = [Chem.MolFromSmiles(smiles) for smiles in file['SMILES_canonical']]
print(mols)

radius=3
nBits=1024
ECFP6 = [AllChem.GetMorganFingerprintAsBitVect(x, radius=radius, nBits=nBits) for x in mols]
print(ECFP6)
