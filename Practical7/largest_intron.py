import re
# define the sequence
seq = 'ATGCAAGTGGTGTGCTGTTTCTGAGAGGGCCTAA'
# search for introns using regex
introns = re.findall(r'GT.*?AG', seq)
# initialize variables to track the largest intron
max_length = 0
largest_intron = None
# iterate through each intron to find the largest one
for intron in introns:
    length = len(intron)
    if length > max_length:
        max_length = length
        largest_intron = intron
# print the results
if largest_intron is not None:
    print(f"The largest intron is: {largest_intron}")
    print(f"The length of the largest intron is: {max_length}")
else:
    print("No intron found in the sequence.")