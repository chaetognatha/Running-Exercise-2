#!usr/bin/python3
"""
    Title: Running Exercise II: dna2aa
    Version: 1
    Date: 2020-10-11
    Author(s): Mattis Knulst

    Description:


    List of functions:
        get_fasta() extracts headers and sequences in a fasta file and returns them as a dictionary
        count_aas() takes an amino acid string and returns absolute counts of amino acids

    List of "non standard" modules:
        No non standard modules are used in the program.

    Procedure:


    Usage:
         python dna2aa.py DNA.faa output_file.txt
"""
def get_fasta(fh=r"output.txt"): # see dna2aa.py
    fasta_dict = {}
    with open(fh) as f:
        for line in f:
            if ">" in line:
                key = line.rstrip()
                value = next(f)
            fasta_dict[key] = value.rstrip()
    return fasta_dict


def count_aas(aa_seq):
    v_aa = ['A', 'R', 'N', 'D', 'B', 'C', 'E', 'Q', 'Z', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y',
            'V'] # list of amino acids
    count_d = {} # declare empty dictionary
    aa_seq_str = str(aa_seq).upper() #make sure sequence is a string and is uppercase
    for i in v_aa: # iterate over list of amino acids
        count_d[i] = aa_seq_str.count(i) # count occurences of that letter in string and return as value with amino acid as key
    return count_d


fasta_dict = get_fasta() # fasta goes here
with open("out_aa_count.txt", "w") as f: # open output file
    for keys in fasta_dict.keys(): # loop over keys
        print(keys, file=f) #write the header
        count_aa_d = count_aas(fasta_dict[keys]) #send the sequence to counting function
        for key, val in count_aa_d.items(): # print all the counted amino acids to file
            print(key, val, file=f)
