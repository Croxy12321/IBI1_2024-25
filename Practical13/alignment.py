# Define a function to load the BLOSUM62 matrix into a dictionary
def load_blosum62(filepath):
    matrix = {} # Create an empty dictionary to store substitution scores
    with open(filepath, 'r') as file:
        lines = []
        for line in file:
          line = line.strip() # Remove leading/trailing whitespace
          # Ignore comment lines and empty lines
          if not line.startswith('#') and line:
            lines.append(line)  

    header = lines[0].split() # First line is the column amino acid headers
    # Process each remaining line in the matrix
    for line in lines[1:]:
        parts = line.split() # Split line into row label + scores
        row_aa = parts[0] # First element is the row amino acid
        scores = list(map(int, parts[1:])) # Convert score strings to integers
        for col_aa, score in zip(header, scores):
                # Store score in dictionary with (row_aa, col_aa) as key
                matrix[(row_aa, col_aa)] = score
    return matrix

# Define a function to read a sequence
def read_fasta(filepath):
    sequence = ''
    with open(filepath, 'r') as file:
        for line in file:
            if not line.startswith('>'): # Skip FASTA header lines
                sequence += line.strip() # Append sequence lines without line breaks
    return sequence

# Define a function to align two sequences using the BLOSUM62 matrix
def align_sequences(seq1, seq2, blosum):
    score = 0 # Initialize total alignment score
    identical = 0 # Initialize counter for identical amino acids
    length = min(len(seq1), len(seq2))  # Ensure sequences are aligned up to the shortest length

    # Compare sequences position by position
    for a1, a2 in zip(seq1[:length], seq2[:length]):
        score += blosum.get((a1, a2), -4)  # Add BLOSUM score and use -4 as default penalty if pair not found
        if a1 == a2:
            identical += 1 # Count how many amino acids are exactly the same

    percent_identity = (identical / length) * 100 # Calculate percentage identity
    return score, percent_identity # Return both total score and percent identity


# Load BLOSUM62 matrix
blosum = load_blosum62("C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical13/blosum62.txt")
# Read sequences 
human_seq = read_fasta("C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical13/human_sod2.fasta")
mouse_seq = read_fasta("C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical13/mouse_sod2.fasta")
random_seq = read_fasta("C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical13/random.fasta")

# Compare human with mouse
print("Human vs Mouse:")
score, identity = align_sequences(human_seq, mouse_seq, blosum)
print(f"Score: {score}, Identity: {identity:.2f}%\n")

# Compare human with random
print("Human vs Random:")
score, identity = align_sequences(human_seq, random_seq, blosum)
print(f"Score: {score}, Identity: {identity:.2f}%\n")

# Compare mouse with random
print("Mouse vs Random:")
score, identity = align_sequences(mouse_seq, random_seq, blosum)
print(f"Score: {score}, Identity: {identity:.2f}%\n")
