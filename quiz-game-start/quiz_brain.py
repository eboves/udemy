from re import I


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        if len(self.question_list) > self.question_number:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(answer, current_question.answer)
    
    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong")

        print(f"The corret answer is: {correct_answer}")
        print(f"Your score now is: {self.score}/{self.question_number}")
        print("\n")
        
        