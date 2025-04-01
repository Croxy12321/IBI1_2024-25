import re
# let user input the splice combination
splice_combination = input("Enter the splice combination (GTAG, GCAG, ATAC): ").strip()
output_file = f'{splice_combination}_spliced_genes.fa'
# open the file and read lines
with open('C:/Users/27661/Downloads/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r',encoding='utf-8') as infile:
    lines = infile.readlines()
# initialize variables
current_gene = None
current_sequence = []
spliced_genes = []
# process each line in the file
for line in lines:
    line = line.strip()
    if line.startswith('>'):
        # if it is a new gene, process the previous one
        if current_gene is not None and current_sequence:
            # detect if the sequence contains the splice combination
            sequence = ''.join(current_sequence)
            if re.search(rf'{splice_combination}', sequence):
                # count TATA boxes
                tata_count = len(re.findall(r'TATA[AT][AT]', sequence))
                if tata_count > 0:
                    spliced_genes.append((current_gene, tata_count, sequence))
        # new gene
        current_gene_1 = line[1:].split()[0]  # get gene names
        current_gene = re.sub(r'_mRNA','',current_gene_1)  # remove '_mRNA' from gene name
        current_sequence = []
    else:
        # add the sequence line
        current_sequence.append(line)
# handle the last gene
if current_gene is not None and current_sequence:
    sequence = ''.join(current_sequence)
    if re.search(rf'{splice_combination}', sequence):
        tata_count = len(re.findall(r'TATA[AT][AT]', sequence))
        if tata_count > 0:
            spliced_genes.append((current_gene, tata_count, sequence))
# write the spliced genes to the output file in specific path
path_1 = r'C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical7/GTAG_spliced_genes.fa'
path_2 = r'C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical7/GCAG_spliced_genes.fa'
path_3 = r'C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical7/ATAC_spliced_genes.fa'
if splice_combination == 'GTAG':
    output_file = path_1
elif splice_combination == 'GCAG':
    output_file = path_2
elif splice_combination == 'ATAC':
    output_file = path_3
else:
    print("Invalid splice combination. Please enter GTAG, GCAG, or ATAC.")
    exit()
with open(output_file, 'w') as outfile:
    for gene, count, sequence in spliced_genes:
        outfile.write(f'>{gene} TATA_count={count}\n{sequence}\n')
