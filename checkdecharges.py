#!/usr/bin/env python3
import sys
import csv
from pathlib import Path
import argparse

def main():
    parser = argparse.ArgumentParser(description='Chemin où trouver le tableau.')
    parser.add_argument('input',
                    help='Entrez la source au format CSV.')

    args = parser.parse_args()

    with open(args.input,newline='') as csvfile:
        fichier = csv.DictReader(csvfile,delimiter=',',quotechar='"')
        prevRow = None
        line = 0
        rows = list(fichier)
        for row in rows:
            line += 1
            if row['Nom'] == rows[line-2]['Nom'] and row['Prénom'] == rows[line-2]['Prénom'] and row['RNE'] != rows[line-2]['RNE']:
                print(f"Erreur de RNE à la ligne {line} pour {row['Prénom']} {row['Nom']}")
            if row['Prénom'] == rows[line-2]['Prénom'] and row['RNE'] == rows[line-2]['RNE'] and row['Nom'] != rows[line-2]['Nom']:
                print(f"Erreur de NOM à la ligne {line} pour {row['Prénom']} {row['Nom']}")
            if row['Nom'] == rows[line-2]['Nom'] and row['RNE'] == rows[line-2]['RNE'] and row['Prénom'] != rows[line-2]['Prénom']:
                print(f"Erreur de PRÉNOM à la ligne {line} pour {row['Prénom']} {row['Nom']}")

if __name__ == "__main__":
    main()
