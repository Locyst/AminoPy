from funcs import DNA2RNA, is_valid_sequence, get_amino_acid
from LocystSelection import Selection, basic_functions

def short_select():
  options = {
    'Shorthand. Example, Arg-Iso-Gly-Thr': basic_functions.true_function,
    'Longhand. Exmaple, Arginine-Isoleucine-Glycine-Threonine': basic_functions.false_function,
  }
            
  selection = Selection("Would you like the Amino Acid names shortened or full? Use the character 'v' to move down and the character '^' to move up", **options)

  getting_selection = True
  while getting_selection:
    print(selection.get_message())
    user_input = input("> ")
    if user_input in ['v', '^']:
        if user_input == 'v':
            selection.move_curser(1)
        elif user_input == '^':
            selection.move_curser(-1)
    elif not user_input:
        getting_selection = False

  return selection.run_at_cursor()

while True:
  DNAstart = False
  sequence = input("Input sequence\n> ")
  if 't' in sequence or 'T' in sequence:
      sequence = DNA2RNA(sequence)
      DNAstart = True

  print()
  short = short_select()

  is_valid_sequence(sequence)

  if DNAstart: print('RNA Sequence,', sequence)
  result = get_amino_acid(sequence, short)
  print("Amino Acid sequence:", result)
  if 'Unknown' in result: print('The Unknown codone could be result to you accidently inputting an extra character')
