from random import choice
import os

from funcs import DNA2RNA, get_amino_acid, is_valid_sequence, round_down_to_multiple
from LocystSelection import basic_functions, UP_ARROW, DOWN_ARROW
from LocystSelection.Selection import Selection


def short_select():
  options = {
    'Shorthand. Example, Arg-Iso-Gly-Thr': basic_functions.return_true,
    'Longhand. Exmaple, Arginine-Isoleucine-Glycine-Threonine': basic_functions.return_false,
  }
            
  selection = Selection(question="Would you like the Amino Acid names shortened or full? Use the arrow keys and click enter to select your option", **options)

  args = None
  while True:
      os.system('clear')
      print(selection.get_message())
      user_input = input("> ")
      if not user_input:        
          print(selection.run_at_cursor(*args))
          break

      elif user_input == UP_ARROW:
          selection.move_curser(move_amount=-1)
      elif user_input == DOWN_ARROW:
          selection.move_curser(move_amount=1)
      else:
          print('invalid choice')

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

def ROUND_SELECT(original, amount):
  def return_original(): return original
  def return_amount(): return amount
  question = f'The amount you entered, {original}, can be rounded down to {amount}. Would you like to do that?'
  options = {
    'Round down': return_original,
    'Keep original': return_amount
  }

  selection = Selection(message=question, **options)

  args = None
  while True:
      os.system('clear')
      print(selection.get_message())
      user_input = input("> ")
      if not user_input:        
          print(selection.run_at_cursor(*args))
          break

      elif user_input == UP_ARROW:
          selection.move_curser(move_amount=-1)
      elif user_input == DOWN_ARROW:
          selection.move_curser(move_amount=1)
      else:
          print('invalid choice')

  return selection.run_at_cursor()

def DNA_RNA_GENERATOR():
  print()
  question = 'Would you like to generate a random DNA or RNA sequence? Use the character "v" to move down and the character "^" to move up'
  options = {
    "DNA": basic_functions.return_true,
    "RNA": basic_functions.return_false
  }

  selection = Selection(message=question, **options)

  args = None
  while True:
      os.system('clear')
      print(selection.get_message())
      user_input = input("> ")
      if not user_input:        
          print(selection.run_at_cursor(*args))
          break

      elif user_input == UP_ARROW:
          selection.move_curser(move_amount=-1)
      elif user_input == DOWN_ARROW:
          selection.move_curser(move_amount=1)
      else:
          print('invalid choice')
      
  amount = int(input('\nHow long do you want the sequence to be?\n> '))

  rounded_amount = round_down_to_multiple(amount, 3)
  if rounded_amount:
    if ROUND_SELECT(amount, rounded_amount):
      amount = rounded_amount

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
    question = "WHat would you like to do? Use the arrow keys and click enter to select your option"
    options = {
      "DNA/RNA to Amino Acid": DNA_RNA2AMINO,
      "Random DNA/RNA Sequence Generator": DNA_RNA_GENERATOR,
      "GC Content": GC_CONTENT,
    }

    selection = Selection(message=question, **options)

    args = None
    while True:
        os.system('clear')
        print(selection.get_message())
        user_input = input("> ")
        if not user_input:        
            print(selection.run_at_cursor(*args))
            break

        elif user_input == UP_ARROW:
            selection.move_curser(move_amount=-1)
        elif user_input == DOWN_ARROW:
            selection.move_curser(move_amount=1)
        else:
            print('invalid choice')

    selection.run_at_cursor()
