def laba(num):
    try:
        result = 100 / num
        return result
    except ValueError:
        print("Ошибка: введено не число")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль или число равно нулю")

user_num = input("Введите число: ")
try:
    user_num = int(user_num)
    if laba(user_num):
        print(f"Результат деления 100 на {user_num}: {laba(user_num)}")
except ValueError:
    print("Ошибка: введено не число")