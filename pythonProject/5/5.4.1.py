
import random
a = ['Бесова', 'Булашева', 'Анисимова', 'Павлова', 'Налетова']
b = ['Шарипова', 'Исхаков', 'Иванова', 'Елизарова', 'Сергеев']
v = a + b
print("Все студенты: ", ', '.join(v), '\n')

random.shuffle(a)
while len(a) < 5:
    a.append(random.randint(0, 5))
x = a[:3:]

random.shuffle(b)
while len(b) < 5:
    b.append(random.randint(0, 5))
y = b[:3:]

c = x + y
c = sorted(c)
print("Члены спортивной команды: ", ', '.join(c))
print(len(c), '\n')

if 'Иванова' in c:
    print("Студент Иванова входит в список членов спортивной команды.")
else:
    print("Студент Иванова не входит в список членов спортивной команды.")
print(c.count("Иванова"))
