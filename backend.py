import os, sys
from PIL import Image

f = open("albums.txt")

titles = f.readlines()

image_template = "https://coverartarchive.org/release-group/~A/front-250.jpg"