import random

mistakes = 0
correct_answers = 0

while mistakes < 3:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 + num2
    user_answer = input(f"{num1} + {num2} = ")
    if int(user_answer) == answer:
        print("Правильно!")
        correct_answers += 1
    else:
        print("Ответ неверный")
        mistakes += 1

print(f"Игра окончена. Правильных ответов: {correct_answers}")