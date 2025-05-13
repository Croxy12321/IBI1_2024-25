def most_frequent_trinucleotide(mrna_sequence):
    count_dict = {}  
    stop_codons = {"UAA", "UAG", "UGA"}
    
    for i in range(0, len(mrna_sequence) - 2, 3):
        codon = mrna_sequence[i:i+3]
        if codon in stop_codons:
            continue  
        if codon in count_dict:
            count_dict[codon] += 1
        else:
            count_dict[codon] = 1

    
    max_count = 0
    most_frequent_codon = None
    for codon, count in count_dict.items():
        if count > max_count:
            max_count = count
            most_frequent_codon = codon

    return most_frequent_codon

codon_table = {
    'AUG': 'Methionine', 
    'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
    'UUA': 'Leucine', 'UUG': 'Leucine',
    'CUU': 'Leucine', 'CUC': 'Leucine', 'CUA': 'Leucine', 'CUG': 'Leucine',
    'AUU': 'Isoleucine', 'AUC': 'Isoleucine', 'AUA': 'Isoleucine',
    'GUU': 'Valine', 'GUC': 'Valine', 'GUA': 'Valine', 'GUG': 'Valine',
    'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
    'AGU': 'Serine', 'AGC': 'Serine',
    'CCU': 'Proline', 'CCC': 'Proline', 'CCA': 'Proline', 'CCG': 'Proline',
    'ACU': 'Threonine', 'ACC': 'Threonine', 'ACA': 'Threonine', 'ACG': 'Threonine',
    'GCU': 'Alanine', 'GCC': 'Alanine', 'GCA': 'Alanine', 'GCG': 'Alanine',
    'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
    'CAU': 'Histidine', 'CAC': 'Histidine',
    'CAA': 'Glutamine', 'CAG': 'Glutamine',
    'AAU': 'Asparagine', 'AAC': 'Asparagine',
    'AAA': 'Lysine', 'AAG': 'Lysine',
    'GAU': 'Aspartic acid', 'GAC': 'Aspartic acid',
    'GAA': 'Glutamic acid', 'GAG': 'Glutamic acid',
    'UGU': 'Cysteine', 'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'CGU': 'Arginine', 'CGC': 'Arginine', 'CGA': 'Arginine', 'CGG': 'Arginine',
    'AGA': 'Arginine', 'AGG': 'Arginine',
    'GGU': 'Glycine', 'GGC': 'Glycine', 'GGA': 'Glycine', 'GGG': 'Glycine'}
def codon_to_amino_acid(most_frequent_codon):
    if most_frequent_codon in codon_table:
       return codon_table[most_frequent_codon]
    else:
       return 'Unknown'
print ('This condon is '+codon_to_amino_acid(most_frequent_codon))

import matplotlib.pyplot as plt

def plot_amino_acid_frequencies(mrna_sequence):
    amino_acid_count = {}  
    stop_codons = {"UAA", "UAG", "UGA"}
    

    for i in range(0, len(mrna_sequence) - 2, 3):
        codon = mrna_sequence[i:i+3]
        if codon in stop_codons:
            continue  
        amino_acid = codon_table[codon]
        if amino_acid in amino_acid_count:
            amino_acid_count[amino_acid] += 1
        else:
            amino_acid_count[amino_acid] = 1

    plt.figure(figsize=(12, 6))
    plt.bar(amino_acid_count.keys(), amino_acid_count.values())
    plt.xlabel('Amino Acids')
    plt.ylabel('Frequency')
    plt.title('Amino Acid Frequency Distribution')
    plt.xticks(rotation=90) 
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
