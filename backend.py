import os, sys
from PIL import Image
import urllib.request

#urllib.request.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "local-filename.jpg")

f = open("albums.txt")

titles = f.readlines()

def save_images():
    for mbid in titles:
        image_template = f"https://coverartarchive.org/release-group/{mbid}/front-250.jpg"
        urllib.request.urlretrieve(image_template, f"{mbid},jpg")

save_images()