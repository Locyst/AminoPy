from amino_acid_combos import amino_acid_combos

def get_amino_acid(sequence, short):
    amino_acid = ""
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        if len(codon) == 3 and codon[0] in amino_acid_combos and codon[1] in amino_acid_combos[codon[0]] and codon[2] in amino_acid_combos[codon[0]][codon[1]]:
            acid = amino_acid_combos[codon[0]][codon[1]][codon[2]]
            if short and acid.lower() != 'stop': acid = acid[0:3]
            amino_acid += acid + '-'
        else:
            amino_acid += "Unknown" + "-"
    return amino_acid[:-1]  # Remove the last hyphen

def DNA2RNA(sequence):
    return_str = ''
    for character in sequence:
        if character.lower()   == 'g': return_str += 'C'
        elif character.lower() == 't': return_str += 'A'
        elif character.lower() == 'a': return_str += 'U'
        elif character.lower() == 'c': return_str += 'G'
        else: raise ValueError("Invalid nucleotide: " + character)
    if len(return_str) != len(sequence): raise ValueError("Invalid DNA sequence length")
    return return_str
