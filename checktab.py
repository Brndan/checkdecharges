#/usr/bin/env python3
import sys
import csv
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description='Chemin où trouver le tableau.')
parser.add_argument('input',
                    help='Entrez la source au format CSV.')

args = parser.parse_args()

if args.input:
    source_folder = Path(args.input)
    print("Je cherche dans : " + args.input)
else:
    print("Impossible de trouver la source")

sys.exit()

with open('perm.csv',newline='') as csvfile:
    fichier = csv.reader(csvfile,delimiter=',',quotechar='"')
    #for jour in {'lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche'}:
    for row in fichier:
        for column in range(5,9):
            print(row[column])
