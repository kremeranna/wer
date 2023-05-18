from PIL import Image, ImageFilter

filenames = ["3.jpg"]
for file in filenames:
    with Image.open(file) as img:
        img.load()
        new_img = img.filter(ImageFilter.BLUR) and img.rotate(90)
        new_img.show()
        new_img.save("new_" + file)