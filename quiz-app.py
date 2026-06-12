questions=[
    {"question":"What  is the capital of India?",
     "answer":"C",
     "options":["A.Mumbai","B.Chennai","C.Delhi","D.Kolkata"]},
    {"question":"What is the language used by or in Pycharm?",
     "answer":"A",
     "options":["Python","Java","C++","JavaScript"]},
    {"question":"2**2=?",
     "answer":"C",
     "options":["2","16","4","8"]}
]

score=0

for q in questions:
    print("\n"+q["question"])
    for option in q["options"]:
        print(option)
    user_answer=input("Enter your answer: ").upper()

    if user_answer==q["answer"]:
        print("Correct!")
        score+=1
    else:
        print("Wrong!")

print("Your score is",score,"/",len(questions))

