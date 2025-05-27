import re

# let user input the splice combination
splice_combination = input("Enter the splice combination (GTAG, GCAG, ATAC): ").strip().upper()
if splice_combination not in ['GTAG', 'GCAG', 'ATAC']:
    print("Invalid splice combination. Please enter GTAG, GCAG, or ATAC.")
    exit()

# define the splice donor and acceptor based on input
donor = splice_combination[:2]
acceptor = splice_combination[2:]

# open the fasta file and read lines
input_file = open('C:/Users/27661/Downloads/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
lines = input_file.readlines()
input_file.close()

# initialize variables
genes = []  # store tuples of (gene_name, tata_count, full_sequence)
current_gene_name = None
current_sequence = ""

# loop through each line to extract gene name and full sequence
for line in lines:
    line = line.strip()
    if line.startswith('>'):
        # if there's an existing sequence, process it first
        if current_gene_name and current_sequence:
            introns = re.findall(f'{donor}.*?{acceptor}', current_sequence)
            # find the largest intron and count TATA boxes inside it
            if introns:
                largest_intron = max(introns, key=len)
                tata_count = len(re.findall(r'TATA[AT]A[AT]', largest_intron))
                if tata_count > 0:
                    genes.append((current_gene_name, tata_count, current_sequence))
        # extract new gene name
        match = re.search(r'gene:(\S+)', line)
        current_gene_name = match.group(1) if match else None
        current_sequence = ""
    else:
        current_sequence += line.upper()  # append sequence part (in uppercase for consistency)

# process the last gene
if current_gene_name and current_sequence:
    introns = re.findall(f'{donor}.*?{acceptor}', current_sequence)
    if introns:
        largest_intron = max(introns, key=len)
        tata_count = len(re.findall(r'TATA[AT]A[AT]', largest_intron))
        if tata_count > 0:
            genes.append((current_gene_name, tata_count, current_sequence))

# set the specific output path based on splice combination
output_paths = {
    'GTAG': r'C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical7/GTAG_spliced_genes.fa',
    'GCAG': r'C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical7/GCAG_spliced_genes.fa',
    'ATAC': r'C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical7/ATAC_spliced_genes.fa'
}

# write results to fasta file
with open(output_paths[splice_combination], 'w') as output_file:
    for gene_name, tata_count, sequence in genes:
        output_file.write(f'>{gene_name} tata_count={tata_count}\n{sequence}\n')
