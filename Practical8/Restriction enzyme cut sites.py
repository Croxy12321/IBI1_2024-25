import re
# input the sequence and the recognition sequence
sequence = input("Enter the DNA sequence: ")
recognition_sequence = input("Enter the recognition sequence: ")
# check if the recognition sequence and the recognition sequence are all A,T,C,G
if not re.match(r'^[ATCG]+$', sequence):
    print("Invalid sequence. Please enter a sequence containing only A, T, C, G.")
    exit()
if not re.match(r'^[ATCG]+$', recognition_sequence):
    print("Invalid recognition sequence. Please enter a sequence containing only A, T, C, G.")
    exit()
# check if the recognition sequence is in the sequence
if not re.search(recognition_sequence, sequence):
    print("The recognition sequence is not found in the sequence.")
    exit()
# create a function to find the recognition sequence in the sequence
def find_recognition_sequence(sequence, recognition_sequence):
    cut_sites = []
    recognition_sequence_length = len(recognition_sequence)
    sequence_length = len(sequence)
    for i in range(sequence_length - recognition_sequence_length + 1):
        if sequence[i:i + recognition_sequence_length] == recognition_sequence:
            cut_sites.append(i+1)
    return cut_sites
# call the function
cut_sites = find_recognition_sequence(sequence, recognition_sequence)
# print the results
print(f"The recognition sequence {recognition_sequence} is found at the following positions: {cut_sites}")