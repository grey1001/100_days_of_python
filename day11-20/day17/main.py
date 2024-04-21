from question_model import Question
from data import trivia
from quiz_brain import QuizBrain
question_bank = []

for question in trivia:
    new_q = Question(question['question'], question['correct_answer'])
    question_bank.append(new_q)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    final_score = quiz.score
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {final_score}/{quiz.question_number}")


