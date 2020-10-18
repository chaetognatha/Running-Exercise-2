#!usr/bin/python3

"""
    Title: Running Exercise II: barcode.py
    Version: 1
    Date: 2020-10-18
    Author(s): Mattis Knulst

    Description: This program will parse a fastq and take the headers and sequences and look for sequences starting with
    a given list of barcodes. The barcoded sequences are put in one file together and non-barcoded sequences are put in
    another. The argument output.txt will currently collect all barcoded samples. The code could easily be extended
    to take arguments for separate sample files by adding argv[x] to the outputs of the tests for barcodes.


    List of functions:
        get_fastq() is a modification of get_fasta() which extracts headers and sequences from a fastq to a dictionary

    List of "non standard" modules:
        No non standard modules are used in the program.

    Procedure:
    1. extract headers and sequences using get_fastq
    2. open two output files for sorting barcoded and not barcoded
    3. test for barcodes in barcodes_list and send sequences (trimmed from barcodes) and headers to appropriate files
    4. if no barcodes are found put in a separate file


    Usage:
         python barcode.py input_filename output_file.txt
"""
import sys

barcodes_list = ['TATCCTCT', 'GTAAGGAG', 'TCTCTCCG']  # list of possible barcodes
barcode_in = sys.argv[1] # "barcode.fastq"
barcode_out = sys.argv[2] # "output_file.txt"

def get_fastq(fh):
    fa_dict = {}
    count_var = 0
    with open(fh, 'r') as in_f:
        for line in in_f:
            if count_var == 0:  # first line is expected to be a header
                header = line.rstrip()
                seq = next(in_f).strip()
                fa_dict[header] = seq
                count_var += 1  # after extracting firs line, increase counter by 1
            elif count_var % 3 == 0:  # if the counter is evenly divisible by 3
                header = line.rstrip()
                seq = next(in_f).strip()
                fa_dict[header] = seq
                count_var += 1  # increase line counter
            else:
                count_var += 1  # even if nothing happens still have to increase that counter
        return fa_dict


fq_dict = get_fastq(barcode_in)

with open(barcode_out, 'w') as bar_out, open('no_barcode_out', 'w') as no_bar_out:  # open two output files
    for key, value in fq_dict.items():
        if value.startswith(barcodes_list[0]):  # test for a barcode in the list
            print(key, value[8:], file=bar_out, sep="\n")  # if true, send to the barcode output
        elif value.startswith(barcodes_list[1]):
            print(key, value[8:], file=bar_out, sep="\n")
        elif value.startswith(barcodes_list[2]):
            print(key, value[8:], file=bar_out, sep="\n")
        else:
            print(key, value, file=no_bar_out, sep="\n")  # otherwise, put it in the other file
