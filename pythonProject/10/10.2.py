import json
with open("../product.json", "r")  as f:
    data = json.load(f)

for i in data["b"]:
    print("Название:", i["name"])
    print("Цена:", i['price'])
    print("Вес:", i['weight'])
    print("В наличии" if i['available'] else "Нет в наличии")

newi = {}
newi['name'] = input("Название продукта:")
newi['price'] = int(input("Цена продукта:"))
newi['weight'] = int(input('Вес продукта:'))
print("Товар есть в наличии")