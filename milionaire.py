#!/usr/bin/python3
from random import randint, shuffle

QUESTIONS_COUNT = 5
# Here is the help functions
# List of game questions
questions = [
	"What is the capital of France?Paris,Berlin,Marseille,Moscow",
	"What is the capital of Spain?Madrid,Berlin,Marseille,Moscow",
	"What is the capital of Portugal?Lisbon,Berlin,Marseille,Moscow",
	"What is the capital of Norway?Oslo,Berlin,Marseille,Moscow",
	"What is the capital of Canada?Ottawa,Berlin,Marseille,Moscow",
	"What is the capital of USA?Washington,Berlin,Marseille,Moscow",
	"What is the capital of China?Beijing,Berlin,Marseille,Moscow",
	"What is the capital of Armenia?Yerevan,Berlin,Marseille,Moscow",
	"What is the capital of Belarus?Minsk,Berlin,Marseille,Moscow",
	"What is the capital of Australia?Canberra,Berlin,Marseille,Moscow",
]

indexes = []
while len(indexes) < QUESTIONS_COUNT:
  ind = randint(0, len(questions)-1)
  if ind not in indexes:
    indexes.append(ind)

# Get random 5 questions for the game
game_questions_list = [questions[ind] for ind in indexes]

final_questions = []
for question in game_questions_list:
  tmp = {}
  q,a = question.split("?")
  tmp["question"] = q+"?"
  variants = a.split(",")
  tmp["correct"] = variants[0]
  shuffle(variants)
  tmp["variants"] = variants
  final_questions.append(tmp)

count = 0
print("Start the game!")
for qobj in final_questions:
  print(qobj["question"])
  for v in qobj["variants"]:
    print(v)
  ans = input("Your answer: ")
  if ans == qobj["correct"]:
    count += 1
    print("Correct. You got %d/%d" %(count, len(final_questions)))
  else:
    print("Incorrect. The correct answer was", qobj["correct"]) 
    print("You got %d/%d" %(count, len(final_questions)))
    
print("End of the game! Your final score is: ")
print("%d/%d" %(count, len(final_questions)))

