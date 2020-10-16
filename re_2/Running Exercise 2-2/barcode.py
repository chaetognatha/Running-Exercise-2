barcodes_list = ['TATCCTCT', 'GTAAGGAG', 'TCTCTCCG']
#pattern = re.compile(r'TATCCTCT')
fna_dict = {}
with open(r'C:\Users\matti\PycharmProjects\running_exercise_2\data\practice.fasta', "r") as in_f:
    for line in in_f:
        if line.startswith(">"):
            header = line.rstrip()
            seq = next(in_f).strip()
            fna_dict[header] = seq
with open('barcode_out', 'w') as bar_out, open('no_barcode_out', 'w') as no_bar_out:
    for key, value in fna_dict.items():
        for barcodes in barcodes_list:
            if value.endswith(barcodes):
                value.rstrip(barcodes)
                print(key, value, file=bar_out, sep="\n")
            else:
                print(key, value, file=no_bar_out, sep="\n")

# extract sequences with barcodes
# remove barcode
# print to file

# extract sequences without barcodes
# print to another file
