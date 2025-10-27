#!python

"""
Offline codon optimizer for E. coli K12
Input: your amino acid vaccine construct
Output: codon-optimized DNA sequence (FASTA file)
"""

# Most frequent E. coli K12 codons for each amino acid
codon_table = {
    'A': 'GCG', 'R': 'CGT', 'N': 'AAC', 'D': 'GAT', 'C': 'TGC',
    'Q': 'CAG', 'E': 'GAA', 'G': 'GGG', 'H': 'CAC', 'I': 'ATC',
    'L': 'CTG', 'K': 'AAA', 'M': 'ATG', 'F': 'TTT', 'P': 'CCG',
    'S': 'TCG', 'T': 'ACC', 'W': 'TGG', 'Y': 'TAC', 'V': 'GTG',
    '*': 'TAA'  # stop codon
}

def optimize_to_dna(protein_seq):
    dna_seq = []
    for aa in protein_seq:
        if aa.upper() in codon_table:
            dna_seq.append(codon_table[aa.upper()])
        else:
            dna_seq.append('NNN')  # unknown/reserved
    return ''.join(dna_seq)

if __name__ == "__main__":
    # Your vaccine construct amino acid sequence
    protein_seq = ("GIINTLQKYYCRVRGGRCAVLSCLPKEEQIGKCSTRGRKCCRRKKEAAAKAKFVAAWTLKAAAGPGPGFISFIIVEKKRNTYSGPGPGISFIIVEKKRNTYSRGPGPGITFISFIIVEKKRNTGPGPGSFIIVEKKRNTYSRLGPGPGTFISFIIVEKKRNTYGPGPGGVTRKYKIKSNPLTKGPGPGAVGFLVRTEFKYNDSGPGPGDRINWISAGVFLDSNGPGPGDTLYFPAVGFLVRTEGPGPGGDTLYFPAVGFLVRTGPGPGGDVLTVNPLVVNWRNGPGPGGFLVRTEFKYNDSNCGPGPGKKVRFENTTSDKGKIGPGPGIKTEMRAVIKNSQKPGPGPGIKWAFEIHHRRPRGRGPGPGISTEFSINETLTLDVGPGPGKTEMRAVIKNSQKPKGPGPGPHNHYKSDNTEAAVLAAYAQITAGVALYAAYSIVPNFILVAAYAQITAGVALAAYRTLGYATEDFAAYAIGPPVFTDKAAYGIAIGPPVFAAYDAFLIDRINWAAYAFLIDRINWAAYTITIPANIGLAAYAMDEGYFAYAAYQTAENPVFTVAAYLAMDEGYFAYAAYHTEFNPHNHYAAYLETDDYNGIYAAYHLISIAINVAAYSMIEPLVLAAAYTEIILNPNLAAYKSSELYHIKKKSLYILRQSKQGDYIRNKKSVGILHYEKLKKNTYSRLEDRRVRPTSSGDLYYKKSNGGGYNQHQLALRSIEKGHHHHHH")

    dna_seq = optimize_to_dna(protein_seq)
    print(">codon_optimized_vaccine_EcoliK12")
    print(dna_seq)

    # Save DNA to FASTA file (wrap 60 bases per line)
    with open("codon_optimized_vaccine.fasta", "w") as f:
        f.write(">codon_optimized_vaccine_EcoliK12\n")
        for i in range(0, len(dna_seq), 60):
            f.write(dna_seq[i:i+60] + "\n")

    print("\nSaved codon_optimized_vaccine.fasta successfully!")

