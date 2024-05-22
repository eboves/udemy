from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions = question_data[0]["text"]
answer = question_data[1]["answer"]
# questions = Question()
question_bank = []
q_brain = QuizBrain(question_bank)

for question in question_data:
    text = question["text"]
    answer = question["answer"] 
    question_object = Question(text,answer) 
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")