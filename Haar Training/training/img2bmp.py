import glob, os, sys
from PIL import Image

folder = 'C:/Users/ACER/Downloads/Haar Training/training/positive/rawdata'

for filepath in glob.iglob(os.path.join(folder, '*.jpg')):
    image = Image.open(filepath).convert('RGB').convert('L')
    new_filepath = os.path.splitext(filepath)[0] + '.bmp'
    image.save(new_filepath)

filelist = [ f for f in os.listdir(folder) if f.endswith(".jpg") ]
for f in filelist:
    os.remove(os.path.join(folder, f))
