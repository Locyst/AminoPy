from funcs import *

while True:
  DNAstart = False
  sequence = input("Input sequence\n> ")
  if 't' in sequence or 'T' in sequence:
      sequence = DNA2RNA(sequence)
      DNAstart = True
  short = bool(int(input('1 for short, 0 for long\n> ')))
  if DNAstart: print('RNA Sequence,', sequence)
  result = get_amino_acid(sequence, short)
  print("Amino Acid sequence:", result)
