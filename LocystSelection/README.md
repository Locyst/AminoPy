# LocystSelection

LocystSelection is a Python library that provides a flexible selection interface for multiple choices with ease. It allows users to create selection menus with customizable options and associated functions, making it easy to implement interactive selection processes in Python applications.

## How to Use

- Clone the repository.
- Import the `Selection` class into your Python environment.
- Follow the example code below to create new selection menus and interact with them.

## Usage

```python
from LocystSelection import Selection
import os

def Add(x, y):
  return x + y

def Sub(x, y):
  return x - y

def Times(x, y):
  return x * y

def Div(x, y):
  return x / y

def test2():
  input('test2')

def test4():
  input('test4')

options = {'Addition': Add, 'Subtraction': Sub, 'Multiplication': Times, 'divide': Div}

# Create a selection menu
operation_selection = Selection('What operation would you like to perform for x: 1 and y: 1? Use ^ to go up and v to go down',
                                **options)

# Interact with the selection menu
getting_input = True
x = 1
y = 1
while getting_input:
    os.system('clear')
    print(operation_selection.get_message())
    user_input = input("> ")
    if not user_input:
        getting_input = False
        print(operation_selection.run_at_cursor(x, y))

    elif user_input == "^":
        operation_selection.move_curser(move_amount=-1)
    elif user_input == "v":
        operation_selection.move_curser(move_amount=1)
    else:
        print('invalid choice')
```

## Configuration

The `Selection` class supports the following configurations:

- `message`: The question or prompt to display at the top of the selection menu.
- `options`: A dictionary containing the options available for selection, where the keys are the option names and the values are the associated functions.
