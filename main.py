from funcs import *
import os

while True:
  DNAstart = False
  sequence = input("Input sequence\n> ")
  if 't' in sequence or 'T' in sequence:
      sequence = DNA2RNA(sequence)
      DNAstart = True

  short = bool(input('True or False to shorthand'))

  is_valid_sequence(sequence)

  if DNAstart: print('RNA Sequence,', sequence)
  result = get_amino_acid(sequence, short)
  print("Amino Acid sequence:", result)
