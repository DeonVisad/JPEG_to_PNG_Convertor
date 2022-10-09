import sys
import os
from PIL import Image


folder_to_convert = sys.argv[1]
converted_folder = sys.argv[2]


if not os.path.exists(converted_folder):
    os.makedirs(converted_folder)

for filename in os.listdir(folder_to_convert):
    img = Image.open(f'{folder_to_convert}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{converted_folder}{clean_name}.png', 'png')
    print('complete')

