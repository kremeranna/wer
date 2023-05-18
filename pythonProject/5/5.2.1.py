list = ["1", "2", "3", "3", "5", "5", "6"]
for i in range(len(list) - 1):
    if list[i] == list[i + 1]:
        print('Совпадающее число', list[i])