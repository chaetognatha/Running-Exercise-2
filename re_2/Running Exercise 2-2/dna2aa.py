"""
The script should run like this: dna2aa.py DNA.faa output_file.txt
"""


# defining a function to create a nucleotide - amino acid translation table
from typing import Any, Union


def translation_table(): # RNA version
    bases = "TCUG"
    codons = [a + b + c for a in bases for b in bases for c in bases]
    # the above generates all the possible three letter combinations of the four bases
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codon_table = dict(zip(codons, amino_acids))
    return codon_table


# this function is to translate a nucleotide seq to a amino acid seq
def translate(seq):
    codon_table = translation_table()
    seq = seq.upper().replace('\n', '').replace(' ', '').replace("A", "U")
    aa_seq: str = ''
    for i in range(0, len(seq), 3):
        codon = seq[i: i + 3]
        amino_acid = codon_table.get(codon, '*')
        aa_seq += amino_acid
    return aa_seq


def get_fasta(fh=r"C:\Users\matti\PycharmProjects\bioinfo-project\data\practice.fasta"):
    fasta_dict = {}
    with open(fh) as f:
        for line in f:
            if ">" in line:
                key = line.rstrip()
                value = next(f)
            fasta_dict[key] = value.rstrip()
    # print(fasta_dict)
    return fasta_dict


def output_dict(my_dict, output_file):
    with open(output_file, "w") as out:
        for i in my_dict.items():
            key = str(i[0])
            value = str(i[1])
            print(key, value, sep="\n", file=out)


def translate_io(input_file=r"C:\Users\matti\PycharmProjects\bioinfo-project\data\practice.fasta", output=r"output.txt"):
    fasta_dict = get_fasta(input_file)
    transl_dict = {}
    for key in fasta_dict:
        tr_seq = translate(fasta_dict[key])
        transl_dict[key] = tr_seq
    output_dict(transl_dict, output)


translate_io()
