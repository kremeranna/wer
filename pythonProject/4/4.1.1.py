def laba(num):
    if num % 3 == 0:
        return True
    else:
        return False
user_num = int(input("Введите число: "))
if laba(user_num):
    print("Число делится на 3")
else:
    print("Число не делится на 3")