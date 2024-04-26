from PIL import Image

F_IN = "p7.jpg"
size = (1280, 720)

# the image is resized to fit into a 480x480 square
# padded by white areas
image = Image.open(F_IN)
image = image.convert("RGBA")
image.thumbnail(size, Image.LANCZOS)
img_w, img_h = image.size
new_w = new_h = max(image.size)
background = Image.new('RGBA', size=size, color='white')
bg_w, bg_h = background.size
offset = (int((bg_w - img_w) / 2), int((bg_h - img_h) / 2))  # Convert offset to integers
background.paste(image, offset)
background.save('pp7.png')
