from random import choice

from funcs import DNA2RNA, get_amino_acid, is_valid_sequence
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

def DNA_RNA2AMINO():
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
  if 'Unknown' in result: print('The Unknown amino acid could be result to you accidently inputting an extra character')
  input('Click enter to continue back to main screen\n')

def DNA_RNA_GENERATOR():
  print()
  question = 'Would you like to generate a random DNA or RNA sequence? Use the character "v" to move down and the character "^" to move up'
  options = {
    "DNA": basic_functions.true_function,
    "RNA": basic_functions.false_function
  }

  selection = Selection(question, **options)

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
      
  amount = int(input('\nHow long do you want the sequence to be?\n> '))
  if selection.run_at_cursor():
    print(''.join(choice('GACT') for i in range(amount)))
  else:
    print(''.join(choice('GACU') for i in range(amount)))
  input('Click enter to continue back to main screen\n')

def GC_CONTENT():
  sequence = input("Input sequence\n> ")

  total_gc_num = sum(1 for character in sequence if character.lower() in ['g', 'c'])

  sequence_len = len(sequence)

  gc_percent = total_gc_num / sequence_len * 100

  print(f"The GC Content of the sequence provided is: {gc_percent}%")
  input('Click enter to continue back to main screen\n\n')


if __name__ == '__main__':
  while True:
    question = "WHat would you like to do? Use the character 'v' to move down and the character '^' to move up"
    options = {
      "DNA/RNA to Amino Acid": DNA_RNA2AMINO,
      "Random DNA/RNA Sequence Generator": DNA_RNA_GENERATOR,
      "GC Content": GC_CONTENT,
    }

    selection = Selection(question, **options)

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

    selection.run_at_cursor()
