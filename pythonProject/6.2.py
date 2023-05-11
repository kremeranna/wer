def word_cost(word):
    cost = 0
    for letter in word:
        if letter in 'АВЕИНОРСТ':
            cost += 1
        elif letter in 'ДКЛМПУ':
            cost += 2
        elif letter in 'БГЁЯ':
            cost += 3
        elif letter in 'ЙЫ':
            cost += 4
        elif letter in 'ЖЗХЦЧ':
            cost += 5
        elif letter in 'ШЭЮ':
            cost += 8
        elif letter in 'ФЩЪ':
            cost += 10
    return cost

word = input('Введите слово: ')
cost = word_cost(word)
print('Стоимость слова', word, 'равна', cost, 'очкам.')