from PIL import Image
x = {"Новый год": "new_year.jpg", "День рождения": "birthday.jpg", "Первое сентября":"1sep.jpg", "Масленица":"as.jpg"}
z = input("Какой сейчас праздник? ")
if z in x :
    image = Image.open(x[z])
    image.show()
    image.save("new2_3.jpg")
else:
    print("такой открытки пока нет:/")