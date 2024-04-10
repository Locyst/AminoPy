class Option:
  def __init__(self, label, func):
      self.label = label
      self.function = func
      self.args = func.__code__.co_varnames[:func.__code__.co_argcount]
      self.enabled = True
      if not callable(func): raise TypeError(f"The provided function, {func}, for Option class {label} is not callable")

  def run(self, *args, **kwargs):
      return self.function(*args, **kwargs) if self.args else self.function()

  def __repr__(self):
      return f'{self.label}: {self.function}'