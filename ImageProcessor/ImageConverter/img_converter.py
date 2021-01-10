from PIL import Image
import os

# todo figure out why <func>. auto-complete not working

current_image = Image.open("../Images/pikachu.jpg")
favicon = current_image.resize((16,16))


#favicon.save("pikachu_favicon.ico", "ICO")