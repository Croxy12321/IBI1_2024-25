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
# remove unnecessary content
lines_preliminary_deletion=re.sub(r'_mRNA.+]','',lines)
lines_secondary_deletion=re.sub(r' cdna.+]','',lines_preliminary_deletion)
# merge lines
lines_combination=re.sub('\n','',lines_secondary_deletion)
# separate the lines and generate a list with 'gene name + sequence' as the elements
lines_separation=re.sub(r'(?=>)','\n',lines_combination).split('\n')
# define gene
gene=[]
# find TATA box and add it to the list, and count the number of TATA boxes
if splice_combination == 'GTAG':
  for line in lines_separation:
      if re.search(r'GT.*TATA[AT]A[AT].*AG',line):
           # search for introns using regex
           introns = re.findall(r'GT.*TATA[AT]A[AT].*AG', line)
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
           line_with_count=re.sub(r'>(.{7})',f">\g<1> tata_count={tata_count}",line)
           gene.append(line_with_count)
if splice_combination == 'GCAG':
  for line in lines_separation:
      if re.search(r'GC.*TATA[AT]A[AT].*AG',line):
           # search for introns using regex
           introns = re.findall(r'GC.*TATA[AT]A[AT].*AG', line)
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
           line_with_count=re.sub(r'>(.{7})',f">\g<1> tata_count={tata_count}",line)
           gene.append(line_with_count)
if splice_combination == 'ATAC':
  for line in lines_separation:
      if re.search(r'AT.*TATA[AT]A[AT].*AC',line):
           # search for introns using regex
           introns = re.findall(r'AT.*TATA[AT]A[AT].*AC', line)
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
           line_with_count=re.sub(r'>(.{7})',f">\g<1> tata_count={tata_count}",line)
           gene.append(line_with_count)
# set the specific paths
path_1 = r'C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical7/GTAG_spliced_genes.fa'
path_2 = r'C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical7/GCAG_spliced_genes.fa'
path_3 = r'C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical7/ATAC_spliced_genes.fa'
# turn the list into a string
gene_string='\n'.join(gene)
# separate gene names from sequences
lines_splited=re.sub('>(.{19}\d*)',r'>\1\n',gene_string)
# write the spliced genes to the output file in specific path
if splice_combination == 'GTAG':
    with open(path_1, 'w') as path_1:
        path_1.write(lines_splited)
elif splice_combination == 'GCAG':
    with open(path_2, 'w') as path_2:
        path_2.write(lines_splited)
elif splice_combination == 'ATAC':
    with open(path_3, 'w') as path_3:
        path_3.write(lines_splited)