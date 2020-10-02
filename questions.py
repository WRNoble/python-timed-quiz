class Question:
    answer = None
    text = None

class Add:
    def __init__(self, num1, num2):
        self.text = '{} + {}'.format(num1, num2)
        self.answer = num1 + num2