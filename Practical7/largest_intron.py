import re

def find_largest_intron(sequence):
    # search for introns using regex
    introns = re.findall(r'GT.*?AG', sequence)
    if not introns:
        return None  # no introns found
    # document introns and their lengths
    max_length = 0
    largest_intron = ""
    # find the largest intron
    for intron in introns:
        length = len(intron)
        if length > max_length:
            max_length = length
            largest_intron = intron
    return largest_intron, max_length
# define the sequence
seq = 'ATGCAAGTGGTGTGCTGTTTCTGAGAGGGCCTAA'
# use the function to print the results
largest_intron, largest_intron_length = find_largest_intron(seq)
if largest_intron is not None:
    print(f"The largest intron is: {largest_intron}")
    print(f"The length of the largest intron is: {largest_intron_length}")
else:
    print("No intron found in the sequence.")