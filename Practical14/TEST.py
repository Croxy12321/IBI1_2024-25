# remove unnecessary content
lines_preliminary_deletion=re.sub(r'_mRNA.+]','',lines)
lines_secondary_deletion=re.sub(r' cdna.+]','',lines_preliminary_deletion)
# turn the list into a string
gene_string='\n'.join(gene)

# separate gene names from sequences
lines_splited=re.sub('>(.{19}\d*)',r'>\1\n',gene_string)