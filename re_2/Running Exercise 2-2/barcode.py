import re
barcodes_list = ['TATCCTCT', 'GTAAGGAG', 'TCTCTCCG']
pattern = re.compile(r'TATCCTCT')
fna_dict = {}
with open(r'C:\Users\matti\PycharmProjects\bioinfo-project\data\practice.fasta', "r") as in_f:
    for line in in_f:
        if line.startswith(">"):
            header = line.rstrip()
            seq = next(in_f)
            fna_dict[header] = seq
    print(fna_dict)
for i in fna_dict.keys():
    istring = str(fna_dict[i])
    for b in barcodes_list:
        print(b)
        #if istring.endswith(b)
            print(istring)




#extract sequences with barcodes
#remove barcode
#print to file

#extract sequences without barcodes
#print to another file