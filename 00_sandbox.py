import random

questions = []

for item in range (0, 5):
    num1 = random.randint(1, 12)
    num2 = random.randint(1,12)

    question = "{} * {}".format(num1, num2)
    correct = eval(question)

    user_ans = int(input("{} = ".format(question)))

    if user_ans == correct:
        feedback = "great job"
    else:
        feedback = "Oops - the correct answer was {}".format(correct)

    summary = "{} = {} | {}".format(question, user_ans, feedback)
    questions.append(summary)

print("***  Quiz History ****")
for item in questions:
    print(item)