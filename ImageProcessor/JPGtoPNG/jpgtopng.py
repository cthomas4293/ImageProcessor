from PIL import Image
import sys
import os

input_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
	os.mkdir(output_folder)

for filename in os.listdir(input_folder):
	img = Image.open(f"{input_folder}{filename}")
	clean_img = os.path.splitext(filename)
	img.save(f"{output_folder}{clean_img[0]}.png", "png")
	print("All Done!")


