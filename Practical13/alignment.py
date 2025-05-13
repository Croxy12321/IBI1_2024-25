def load_blosum62(filepath):
    matrix = {}
    with open(filepath, 'r') as file:
        lines = []
        for line in file:
          line = line.strip()
          if not line.startswith('#') and line:
            lines.append(line)  
    header = lines[0].split()
    for line in lines[1:]:
        parts = line.split()
        row_aa = parts[0]
        scores = list(map(int, parts[1:]))
        for col_aa, score in zip(header, scores):
                matrix[(row_aa, col_aa)] = score
    return matrix
def read_fasta(filepath):
    sequence = ''
    with open(filepath, 'r') as file:
        for line in file:
            if not line.startswith('>'):
                sequence += line.strip()
    return sequence

def align_sequences(seq1, seq2, blosum):
    score = 0
    identical = 0
    length = min(len(seq1), len(seq2))  

    for a1, a2 in zip(seq1[:length], seq2[:length]):
        score += blosum.get((a1, a2), -4)  
        if a1 == a2:
            identical += 1

    percent_identity = (identical / length) * 100
    return score, percent_identity

if __name__ == "__main__":
    blosum = load_blosum62("C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical13/blosum62.txt")
    human_seq = read_fasta("C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical13/human_sod2.fasta")
    mouse_seq = read_fasta("C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical13/mouse_sod2.fasta")
    random_seq = read_fasta("C:/Users/27661/Desktop/IBI/IBIP3/IBI1_2024-25/Practical13/random.fasta")

    print("Human vs Mouse:")
    score, identity = align_sequences(human_seq, mouse_seq, blosum)
    print(f"Score: {score}, Identity: {identity:.2f}%\n")

    print("Human vs Random:")
    score, identity = align_sequences(human_seq, random_seq, blosum)
    print(f"Score: {score}, Identity: {identity:.2f}%\n")

    print("Mouse vs Random:")
    score, identity = align_sequences(mouse_seq, random_seq, blosum)
    print(f"Score: {score}, Identity: {identity:.2f}%\n")
