import re
# let user input the splice combination
splice_combination = input("Enter the splice combination (GTAG, GCAG, ATAC): ").strip()
if splice_combination not in ['GTAG', 'GCAG', 'ATAC']:
    print("Invalid splice combination. Please enter GTAG, GCAG, or ATAC.")
    exit()
# open the file
input_file=open('C:/Users/27661/Downloads/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
# read lines
lines=input_file.read()
# merge lines
lines_combination=re.sub('\n','',lines)
# separate the lines and generate a list with 'gene name + sequence' as the elements
lines_separation=re.sub(r'(?=>)','\n',lines_combination).split('\n')
# define gene
gene=[]
tata_counts = [] # list to store the number of TATA boxes for each gene
# find TATA box and add it to the list, and count the number of TATA boxes
if splice_combination == 'GTAG':
  for line in lines_separation:
      if re.search(r'GT.*TATA[AT]A[AT].*AG',line):
           # search for introns using regex
           introns = re.findall(r'GT.*TATA[AT]A[AT].*AG', line)
           gene_name=re.findall(r'gene:(\S+)',line) # extract gene name using regex
           gene_sequence=re.findall(r'](.+)',line) # extract gene sequence using regex
           # initialize variables to track the largest intron
           max_length = 0
           largest_intron = None
           # iterate through each intron to find the largest one
           for intron in introns:
             length = len(intron)
             if length > max_length:
                max_length = length
                largest_intron = intron
                tata_count = len(re.findall(r'TATA[AT]A[AT]', largest_intron))
                tata_counts.append(tata_count) # add the count to the list
           gene.append((gene_name[0],tata_counts[-1],gene_sequence[0])) # add gene name and sequence to the list
if splice_combination == 'GCAG':
  for line in lines_separation:
      if re.search(r'GC.*TATA[AT]A[AT].*AG',line):
           # search for introns using regex
           introns = re.findall(r'GC.*TATA[AT]A[AT].*AG', line)
           gene_name=re.findall(r'gene:(\S+)',line) # extract gene name using regex
           gene_sequence=re.findall(r'](.+)',line) # extract gene sequence using regex
           # initialize variables to track the largest intron
           max_length = 0
           largest_intron = None
           # iterate through each intron to find the largest one
           for intron in introns:
             length = len(intron)
             if length > max_length:
                max_length = length
                largest_intron = intron
                tata_count = len(re.findall(r'TATA[AT]A[AT]', largest_intron))
                tata_counts.append(tata_count) # add the count to the list
           gene.append((gene_name[0],tata_counts[-1],gene_sequence[0])) # add gene name and sequence to the list
if splice_combination == 'ATAC':
  for line in lines_separation:
      if re.search(r'AT.*TATA[AT]A[AT].*AC',line):
           # search for introns using regex
           introns = re.findall(r'AT.*TATA[AT]A[AT].*AC', line)
           gene_name=re.findall(r'gene:(\S+)',line) # extract gene name using regex
           gene_sequence=re.findall(r'](.+)',line) # extract gene sequence using regex
           # initialize variables to track the largest intron
           max_length = 0
           largest_intron = None
           # iterate through each intron to find the largest one
           for intron in introns:
             length = len(intron)
             if length > max_length:
                max_length = length
                largest_intron = intron
                tata_count = len(re.findall(r'TATA[AT]A[AT]', largest_intron))
                tata_counts.append(tata_count) # add the count to the list
           gene.append((gene_name[0],tata_counts[-1],gene_sequence[0])) # add gene name and sequence to the list
# set the specific paths
path_1 = r'C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical7/GTAG_spliced_genes.fa'
path_2 = r'C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical7/GCAG_spliced_genes.fa'
path_3 = r'C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical7/ATAC_spliced_genes.fa'
# write the spliced genes to the output file in specific path
if splice_combination == 'GTAG':
    with open(path_1, 'w') as path_1:
      for line in gene:
        path_1.write(line[0]+' tata_count='+str(line[1])+'\n'+line[2]+'\n')
elif splice_combination == 'GCAG':
    with open(path_2, 'w') as path_2:
      for line in gene:
        path_2.write(line[0]+' tata_count='+str(line[1])+'\n'+line[2]+'\n')
elif splice_combination == 'ATAC':
    with open(path_3, 'w') as path_3:
      for line in gene:
        path_3.write(line[0]+' tata_count='+str(line[1])+'\n'+line[2]+'\n')