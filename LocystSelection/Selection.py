from .Option import Option
from random import choice

class Selection:
  DEFAULT_FORMATS = {
      "Format 1": "{selection} {label}",
      "Format 2": "{label} - {selection}",
      "Format 3": "{selection}: {label}",
      "Format 4": "{label} ({selection})",
      "Format 5": "<{selection}> {label}",
  }
  
  def __init__(self, *, message, format=None, **options):
      names = list(options.keys())
      functions = list(options.values())

      self.message = message or 'Select an option below'

      self.options = [Option(names[i], functions[i]) for i in range(len(options))]

      ####################
      # USER INPUT
      ####################

      self.cursor_pos = 0

      ####################
      # CUSTOMIZATION
      ####################

      self.custom_format = format or choice(list(Selection.DEFAULT_FORMATS.values()))

      self.question_indent_amount = 0
      self.question2choice_separation_amount = 2
      self.choice2choice_separation_amount = 2

      self.unselected_icon = '○'
      self.selected_icon = '●'
      self.questions_per_page = 5

  def _selection_check(self, pos):
      if self.cursor_pos == pos: return self.selected_icon
      return self.unselected_icon

  def move_curser(self, move_amount):
      new_cursor_pos = self.cursor_pos + move_amount
      if -1 < new_cursor_pos < len(self.options):
          self.cursor_pos = new_cursor_pos

  def run_at_cursor(self, *args, **kwargs):
      return self.run(self.cursor_pos, *args, **kwargs)

  def run(self, pos, *args, **kwargs):
      return self.options[pos].run(*args, **kwargs)

  def get_message(self):
      message = ' ' * self.question_indent_amount + self.message

      message += '\n' * self.question2choice_separation_amount

      idx_start = self.cursor_pos - 1
      idx_end = idx_start + self.questions_per_page

      for idx, option in enumerate(self.options):
          if idx >= idx_end:
              message += 'v~v~v~v~v'
              break

          if 'selection' not in self.custom_format:
              raise ValueError('{selection}', 'is not in custom_format, please add this or users cannot tell what they are selecting')
        
          formatted_option = self.custom_format.format(
              selection = self._selection_check(idx),
              label = option.label,
              function = option.function,
              index = idx
          )

          message += formatted_option + '\n' * self.choice2choice_separation_amount

      message = message.strip()

      message += '\n'

      return message

  def option(self, *, name=None):
    def decorator(func):
      Name = name or func.__name__
      self.options.append(Option(Name, func))
      return func
    return decorator