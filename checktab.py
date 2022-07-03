#/usr/bin/env python3

import csv

with open('perm.csv',newline='') as csvfile:
    fichier = csv.reader(csvfile,delimiter=',',quotechar='"')
    #for jour in {'lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche'}:
    for row in fichier:
        for column in range(5,9):
            print(row[column])
