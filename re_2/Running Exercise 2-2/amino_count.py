#!usr/bin/python3
"""
    Title: Running Exercise II: amino count
    Version: 1
    Date: 2020-10-18
    Author(s): Mattis Knulst

    Description: Simple program for counting absolute abundances of amino acids in sequences and printing them to a file
    - the list of amino acids can consist of any string e.g. "A" or "a" or "Ala" or "ala" but must be in one column with
    one string per line.


    List of functions:
        get_fasta() extracts headers and sequences in a fasta file and returns them as a dictionary
        count_aas() takes an amino acid string and returns absolute counts of amino acids

    List of "non standard" modules:
        No non standard modules are used in the program.

    Procedure:
    1. Extract headers and sequences using get_fasta()
    2. open output file
    3. send sequences to be counted in count_aas()
    4. print headers and abundance counts to output file


    Usage:
         python amino_count.py amino.faa amino.list output_file.txt
"""
import sys

amino_faa = sys.argv[1]
amino_list = sys.argv[2]
output_file = sys.argv[3]
def get_fasta(fh): # extract header and seq as key and value in dictionary from file
    fasta_dict = {}
    with open(fh) as f:
        for line in f:
            if line.startswith(">"):
                key = line.rstrip()
                value = next(f)
            fasta_dict[key] = value.rstrip()
    return fasta_dict


def count_aas(aa_seq):
    v_aa = []  # list of amino acids
    with open(amino_list, 'r') as f:
        for line in f:
            v_aa.append(line.rstrip().upper())
    count_d = {} # declare empty dictionary
    aa_seq_str = str(aa_seq).upper() #make sure sequence is a string
    for i in v_aa: # iterate over list of amino acids
        count_d[i] = aa_seq_str.count(i) # count occurences of that letter in string and return as value with amino acid as key
    return count_d


fasta_dict = get_fasta(amino_faa) # fasta goes here
with open(output_file, "w") as f: # open output file
    for keys in fasta_dict.keys(): # loop over keys
        print(keys, file=f) #write the header
        count_aa_d = count_aas(fasta_dict[keys]) #send the sequence to counting function
        for key, val in count_aa_d.items(): # print all the counted amino acids to file
            print(key, val, file=f)

