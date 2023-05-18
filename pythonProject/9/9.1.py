from PIL import Image, ImageFilter
import os

f = ["11.jpg", "22.jpg", "33.jpg", "44.jpg", "55.jpg"]
count = 0
for file in f:
    count += 1
    img = Image.open(file)
    new_img = img.filter(ImageFilter.EMBOSS)
    new_img.show()
    try:
        os.mkdir("Z:\1-MD-15_1\Кремер Анна\pythonProject")
    except:
        pass
    new_img.save("new_" + file)
