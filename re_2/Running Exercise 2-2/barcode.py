#!usr/bin/python3
import re

"""
    Title: Running Exercise II: dna2aa
    Version: 1
    Date: 2020-10-11
    Author(s): Mattis Knulst

    Description:


    List of functions:
        No user defined functions are used in the program.

    List of "non standard" modules:
        No non standard modules are used in the program.

    Procedure:


    Usage:
         python dna2aa.py DNA.faa output_file.txt
"""
barcodes_list = ['TATCCTCT', 'GTAAGGAG', 'TCTCTCCG'] # list of possible barcodes
#pattern = re.compile(r'TATCCTCT')
fna_dict = {}
with open(r'C:\Users\matti\PycharmProjects\running_exercise_2\data\practice.fasta', "r") as in_f: #same as get_fasta()
    for line in in_f:
        if line.startswith(">"):
            header = line.rstrip()
            seq = next(in_f).strip()
            fna_dict[header] = seq
with open('barcode_out', 'w') as bar_out, open('no_barcode_out', 'w') as no_bar_out: # open two output files
    for key, value in fna_dict.items():
        if value.endswith(barcodes_list[0]): # test for a barcode in the list
            print(key, value[:-8], file=bar_out, sep="\n") # if true, send to the barcode output
        elif value.endswith(barcodes_list[1]):
            print(key, value[:-8], file=bar_out, sep="\n")
        elif value.endswith(barcodes_list[2]):
            print(key, value[:-8], file=bar_out, sep="\n")
        else:
            print(key, value, file=no_bar_out, sep="\n") #otherwise, put it in the other file

