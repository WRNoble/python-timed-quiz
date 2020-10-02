import datetime
import random

from questions import Add, Multiply

class Quiz:
    questions = []
    answer = []

    def __init__(self):
        question_types = (Add, Multiply)
        for _ in range (10):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            question = question_types
            self.questions.append()


    def take_quiz(self):

    
    def ask(self, question):

    def total_corret(self):
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
            return total

    def summary(self):
        print("You got {} out of {} correct!".format(self.total_correct(), len(self.questions)))
        print("it took you {} seconds total".format((self.end_time-self.start_time).seconds))