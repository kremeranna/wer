from PIL import Image, ImageDraw, ImageFont
x = {"Новый год": "new_year.jpg", "День рождения": "birthday.jpg", "Первое сентября":"1sep.jpg", "Масленица":"as.jpg"}
z = input("Какой сейчас праздник? ")
if z in x :
    image = Image.open(x[z])
    name = input("Кого поздравляем? ")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 40)
    text = f"{name}, поздравляю!"
    text_width, text_heigh = draw.textsize(text, font)
    xx = (image.width - text_width)/2
    yy = image.height - text_heigh - 50
    draw.text((xx,yy), text, font=font, fill=(255,0,0,255))

    image.show()
    image.save("new2_3.jpg")
else:
    print("такой открытки пока нет:/")