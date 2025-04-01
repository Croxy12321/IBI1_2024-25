import re

# open the file and read lines
with open('C:/Users/27661/Downloads/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r',encoding='utf-8') as infile:
    lines = infile.readlines()

# initialize variables
current_gene = None
current_sequence = []
tata_genes = []

# process each line in the file
for line in lines:
    line = line.strip()
    if line.startswith('>'):
        # if it is a new gene, process the previous one
        if current_gene is not None and current_sequence:
            # detect if the sequence contains TATA box
            sequence = ''.join(current_sequence)
            if re.search(r'TATA[AT][AT]', sequence):
                tata_genes.append((current_gene, sequence))
        # reset for the new gene
        current_gene = line[1:].split()[0]  # get gene name
        current_sequence = []
    else:
        # add the sequence line to the current gene's sequence
        current_sequence.append(line)

# deal with the last gene in the file
if current_gene is not None and current_sequence:
    sequence = ''.join(current_sequence)
    if re.search(r'TATA[AT][AT]', sequence):
        tata_genes.append((current_gene, sequence))
# write the TATA box genes to the Practical7
output_path = r'C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical7/tata_genes.fa'
# write the TATA box genes to the new file
with open(output_path, 'w') as outfile:
    for gene, sequence in tata_genes:
        outfile.write(f'>{gene}\n{sequence}\n')