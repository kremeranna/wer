result = ""
while True:
    word = input("Введите слово: ")
    if word == "stop":
        break
    result += word + " "

if "ф" in result:
    print("Это редкое слово!")
else:
    print("Это не очень редкое слово...")

