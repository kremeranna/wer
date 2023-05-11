from PIL import Image
image = Image.open("../3.jpg")
z = image.crop((300, 300, 500, 500))
image.show()
z.save("crop_3.jpg")