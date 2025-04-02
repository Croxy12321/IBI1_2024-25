import re
# open the file and set output path
input_file=open('C:/Users/27661/Downloads/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
ouput_file=open('C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical7/tata_genes.fa','w')
# read lines
lines=input_file.read()
# remove unnecessary content
lines_preliminary_deletion=re.sub(r'_mRNA.+]','',lines)
lines_secondary_deletion=re.sub(r' cdna.+]','',lines_preliminary_deletion)
# merge lines
lines_combination=re.sub('\n','',lines_secondary_deletion)
# separate the lines and generate a list with 'gene name + sequence' as the elements
lines_separation=re.sub(r'(?=>)','\n',lines_combination).split('\n')
# define gene
gene=[]
# find TATA box and add it to the list
for line in lines_separation:
    if re.search(r'TATA[AT]A[AT]',line):
         gene.append(line) 
# turn the list into a string
gene_string='\n'.join(gene)
# separate gene names from sequences
lines_splited=re.sub(r'>(.{7})',r'>\1\n',gene_string)
# write the output file
ouput_file.write(lines_splited)
# close the files
input_file.close()