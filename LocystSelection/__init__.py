class Option:
    def __init__(self, label, func):
        self.label = label
        self.function = func
        
    def run(self):
        return self.function()

    def __repr__(self):
        return f'{self.label}: {self.function}'

class Selection:
    def __init__(self, message, **options):
        names = list(options.keys())
        functions = list(options.values())

        self.message = message
        self.options = [Option(names[i], functions[i]) for i in range(len(options))]
        
        ####################
        # USER INPUT
        ####################
        
        self.cursor_pos = 0
        
        ####################
        # CUSTOMIZATION
        ####################
        
        self.question_indent_amount = 0
        self.question2choice_separation_amount = 2
        self.choice2choice_separation_amount = 2
        
        self.unselected_icon = '○'
        self.selected_icon = '●'
        self.questions_per_page = 5
        
    def _selection_check(self, pos):
        if self.cursor_pos == pos: return self.selected_icon
        return self.unselected_icon
    
    def move_curser(self, amount):
        new_cursor_pos = self.cursor_pos + amount
        if -1 < new_cursor_pos < len(self.options):
            self.cursor_pos = new_cursor_pos

    def run_at_cursor(self):
        return self.run(self.cursor_pos)

    def run(self, pos):
        return self.options[pos].run()
        
    def get_message(self):
        message = ' ' * self.question_indent_amount + self.message

        message += '\n' * self.question2choice_separation_amount

        idx = 0
        for option in self.options:
            message += ' ' + self._selection_check(idx) + ' ' + option.label + '\n' * self.choice2choice_separation_amount
            idx += 1

        message = message.strip()
        
        message += '\n'

        return message