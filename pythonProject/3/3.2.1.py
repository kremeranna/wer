
result = ""

while True:
    word = input("Введите слово: ")
    if word == "stop":
        break
    result += word + " "

print("Результат:", result)
