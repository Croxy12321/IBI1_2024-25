import re
# open the file and set the output path
input_file = open('C:/Users/27661/Downloads/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output_file = open('C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical7/tata_genes.fa', 'w')

# define gene name and sequence variables
current_gene_name = None
current_sequence = ""

# read the fasta file line by line
for line in input_file:
    line = line.strip()
    # if the line is a description line
    if line.startswith(">"):
        # if the previous sequence exists, check for TATA box
        if current_gene_name and current_sequence:
            if re.search(r'TATA[AT]A[AT]', current_sequence):
                # write to output file in FASTA format
                output_file.write(f">{current_gene_name}\n{current_sequence}\n")
        # extract gene name using regex
        match = re.search(r'gene:(\S+)', line)
        current_gene_name = match.group(1) if match else None
        current_sequence = ""
    else:
        # append the sequence part (convert to uppercase)
        current_sequence += line.upper()

# process the last gene in the file
if current_gene_name and current_sequence:
    if re.search(r'TATA[AT]A[AT]', current_sequence):
        output_file.write(f">{current_gene_name}\n{current_sequence}\n")

# close the files
input_file.close()
output_file.close()
