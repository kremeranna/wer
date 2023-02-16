pas = input('введите пароль')
if len(pas) < 6:
    print('пароль слишком короткий')
elif pas[0:7] == "qwerty":
    print('ненадёжный пароль')
else:
    print('пароль принят')