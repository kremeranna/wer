with open('../data.csv', 'r') as f:
    data = []
    for line in f:
        parts = line.strip().split(',')
        if len(parts) == 3:
            data.append(parts)

total_price = 0

print('Нужно купить:')

for item in data[1:]:
    product = item[0]
    quantity = int(item[1])
    price = int(item[2])
    item_price = quantity * price
    total_price += item_price
    print('{} - {} шт. за {} руб.'.format(product, quantity, item_price))

print('Итоговая сумма: {} руб.'.format(total_price))