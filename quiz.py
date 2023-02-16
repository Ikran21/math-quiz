import random

class MathQuiz:
    def __init__(self, num_questions=5):
        self.score = 0
        self.questions = []
        for i in range(num_questions):
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            op = random.choice(['+', '-', '*', '/'])
            question = f"What is {a} {op} {b}?"
            if op == '+':
                answer = a + b
            elif op == '-':
                answer = a - b
            elif op == '*':
                answer = a * b
            else:
                answer = a / b
            self.questions.append((question, answer))
        random.shuffle(self.questions)

    def run_quiz(self):
        for question, answer in self.questions:
            user_answer = input(question + " ")
            try:
                if float(user_answer) == answer:
                    print("Correct!")
                    self.score += 1
                else:
                    print("Incorrect.")
            except:
                print("Invalid answer.")
        print(f"Your final score is {self.score}/{len(self.questions)}")

quiz = MathQuiz()
quiz.run_quiz()
