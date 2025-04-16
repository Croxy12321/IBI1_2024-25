import re
# open the file and set output path
input_file=open('C:/Users/27661/Downloads/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
ouput_file=open('C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical7/tata_genes.fa','w')
# read lines
lines=input_file.read()
# merge lines
lines_combination=re.sub('\n','',lines)
# separate the lines and generate a list with 'gene name + sequence' as the elements
lines_separation=re.sub(r'(?=>)','\n',lines_combination).split('\n')
# define gene
gene=[]
# find TATA box and add it to the list
for line in lines_separation:
    if re.search(r'TATA[AT]A[AT]',line):
         gene_name=re.findall(r'gene:(\S+)',line) # extract gene name using regex
         gene_sequence=re.findall(r'](.+)',line) # extract gene sequence using regex
         gene.append((gene_name[0],gene_sequence[0])) # add gene name and sequence to the list
# output the result to a file
for line in gene:
    ouput_file.write(line[0]+'\n')
    ouput_file.write(line[1]+'\n')