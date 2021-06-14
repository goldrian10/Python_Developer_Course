from PIL import Image, ImageFilter

# img = Image.open('./static/pikachu.jpg')
#
# filtered_img = img.filter(ImageFilter.SMOOTH_MORE)
# filtered_img = img.convert('L')
# filtered_img.save('./static/greyPikachu.png', 'png')

# crooked = filtered_img.rotate(90)
# crooked.show()

# resize = filtered_img.resize((300, 300))
# resize.show()

# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.show()

img = Image.open('./static/astro.jpg')
print(img.size)
img.thumbnail((400, 400))
img.save('./static/newAstro.jpg')
