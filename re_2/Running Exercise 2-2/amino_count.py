def get_fasta(fh=r"output.txt"):
    fasta_dict = {}
    with open(fh) as f:
        for line in f:
            if ">" in line:
                key = line.rstrip()
                value = next(f)
            fasta_dict[key] = value.rstrip()
    # print(fasta_dict)
    return fasta_dict


def count_aas(aa_seq):
    v_aa = ['A', 'R', 'N', 'D', 'B', 'C', 'E', 'Q', 'Z', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y',
            'V']
    count_d = {}
    aa_seq_str = str(aa_seq).upper()
    for i in v_aa:
        count_d[i] = aa_seq_str.count(i)
    return count_d


fasta_dict = get_fasta()
with open("out_aa_count.txt", "w") as f:
    for keys in fasta_dict.keys():
        print(keys, file=f)
        count_aa_d = count_aas(fasta_dict[keys])
        for key, val in count_aa_d.items():
            print(key, val, file=f)
