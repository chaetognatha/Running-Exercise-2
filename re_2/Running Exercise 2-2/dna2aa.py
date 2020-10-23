#!usr/bin/python3
"""
    Title: Running Exercise II: dna2aa
    Version: 1
    Date: 2020-10-18
    Author(s): Mattis Knulst, Júlia Ortis

    Description: This program translates DNA sequences to amino acid sequences. The step in which the DNA is converted
    to RNA code is more or less useless (since the translation table could be in DNA code), but mean this code would work
    with RNA as well as DNA. The translated sequences are written to specified file. I have tried to follow a functional
    programming paradigm in this script so all operations are packed into functions that are called from a main function
    found at the end of the script.


    List of functions:
        translation_table() will generate a codon-amino acid table as a dictionary
        translate() uses the translation table and converts a DNA string to RNA and then to an amino acid sequence string
        get_fasta() extracts headers and sequences in a fasta file and returns them as a dictionary
        output_dict() takes a dict and prints it to a given output file
        translate_io() is the main function which calls all the above, it takes an input and an output file as arguments


    List of "non standard" modules:
        No non standard modules are used in the program.

    Procedure:
    1. extract headers and sequences from given fasta file
    2. send sequences to translate()
    3. write headers and translated sequences to output file


    Usage:
         python dna2aa.py DNA.faa output_file.txt
"""
import sys
dna_faa = "DNA.faa" #sys.argv[1]
output_file = "amino_out.faa" #sys.argv[2]

# defining a function to create a nucleotide - amino acid translation table
def translation_table(): # RNA version
    nucleotides = "TCUG" # string of RNA letters
    codons = [a + b + c for a in nucleotides for b in nucleotides for c in nucleotides] # list comprehension to generate possible three letter combinations of nts
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG' # string that will correspond to translated codons
    trans_table = dict(zip(codons, amino_acids)) # make a dictionary with the above
    return trans_table


def translate(seq): # take a DNA string
    trans_table = translation_table() # import translation table
    seq = seq.upper().strip().replace("A", "U") # make sure the string is uppercase, remove leading and trailing whitespace, remove any spaces in string and replace A with U
    aa_seq: str = '' # explicitly declare that aa_seq is a string
    for i in range(0, len(seq), 3): # loop over the length of the sequence string, 3 letters at a time
        codon = seq[i: i + 3] # extract the codon
        amino_acid = trans_table.get(codon, '*') # get amino acid or stop value from translation table
        aa_seq += amino_acid #put aas or stops into a string
    return aa_seq


def get_fasta(fh):
    fasta_dict = {}
    with open(fh) as f: # open the given file
        for line in f: # loop over lines in file
            if line.startswith(">"): # find header
                key = line.rstrip() # remove trailing whitespace/newlines
                value = next(f) # following line is the sequence
            fasta_dict[key] = value.rstrip() #build the dictionary of headers and sequences
    return fasta_dict


def output_dict(my_dict, output_file):
    with open(output_file, "w") as out: #open a given file to write to
        for key, value in my_dict.items(): # unpack dictionary
            print(key, value, sep="\n", file=out) # write headers and sequences to file, make new lines for each


def translate_io(input_file, output):
    fasta_dict = get_fasta(input_file) # extract headers and sequences
    transl_dict = {} # declare empty dictionary
    for key in fasta_dict: # loop over the key headers
        tr_seq = translate(fasta_dict[key]) # translate DNA -> amino acids
        transl_dict[key] = tr_seq # put output together in dictionary
    output_dict(transl_dict, output) # send output dictionary and out file to output function


translate_io(dna_faa, output_file)
