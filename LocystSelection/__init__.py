class Option:
    def __init__(self, label, func):
        self.label = label
        self.function = func
        
    def run(self):
        self.function()

class Selection:
    def __init__(self, message, **options):
        self.message = message
        self.options = []
        for name, func in enumerate(options):
            self.options.append(Option(name, func))
        
        ####################
        # USER INPUT
        ####################
        
        self.cursor_pos = 0
        
        ####################
        # CUSTOMIZATION
        ####################
        
        self.question_indent_amount = 0
        self.question_choice_separation_amount = 2
        self.unselected_icon = '○'
        self.selected_icon = '●'
        
    def _selection_check(self, pos):
        if self.cursor_pos == pos: return self.selected_icon
        return self.unselected_icon
        
    def print_(self):
        message = ' ' * self.question_indent_amount + self.message

        for i in range(1, self.question_choice_separation_amount):
            message += '\n'
        
        idx = 0
        for option in self.options.keys():
            message += '\n ' + self._selection_check(idx) + ' ' + option
            idx += 1
            
        print(message)
            
def hello():
    print('hello')
    
def hello2():
    print('hello2')
    
def hello3():
    print('hello3')
            
options = {
    'hello': hello,
    'hello2': hello2,
    'hello3': hello3
}
            
Selection('Hello World', **options).print_()
