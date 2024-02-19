from PIL import Image

image = Image.open("photo.jpg")

percent_resize = 0.4

width_size = int(image.size[0] * percent_resize)
height_size = int(image.size[1] * percent_resize)

image = image.resize((width_size, height_size), Image.BICUBIC)
image.save(f'new.jpeg', 'jpeg', optimize=True, quality=90)


