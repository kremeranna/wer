from PIL import Image
x = "3.jpg"
with Image.open(x) as img:
    img.load()
new_img = img.resize((img.width// 3, img.height// 3))
new_img.save("res_3.jpg")
con_img = img.rotate(180)
con_img.save('flip_3.jpg')
con_img = img.transpose(Image.FLIP_LEFT_RIGHT)
con_img.save('flip2_3.jpg')
