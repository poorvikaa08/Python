from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for qns in question_data:
    q_text = qns['text']
    q_answer = qns['answer']
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)
    
    # question_bank.append(Question(qns['text'], qns['answer']))
    
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.q_number}")
      