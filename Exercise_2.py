# Project 2: Quiz


from my_Questions import Question 

question_prompts = [
    "what is 12 + 13?\n(a)15\n(b)23\n(c)25\n\n",
    "what is 24 * 2?\n(a)21\n(b)48\n(c)100\n\n",
    "what is 41 - 9?\n(a)32\n(b)11\n(c)30\n\n"
]

"""question1 = Question(question_prompts[0], "c")
question2 = Question(question_prompts[1], "b")
question3 = Question(question_prompts[2], "a")"""

questions = [Question(question_prompts[0], "c"),
             Question(question_prompts[1], "b"),
             Question(question_prompts[2], "a") 
            ]

def take_quiz():
    score = 0
    for question in questions:
        user_answer = input(question.prompt)
        if user_answer == question.answer:
            score = score+1

    print("Your score: ", score) 

take_quiz()

      
