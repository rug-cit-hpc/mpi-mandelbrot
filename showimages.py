#!/usr/bin/python3

# use a tkinter label as a panel/frame with a background image
# note that tkinter only reads gif and ppm images
# use the Python Image Library (PIL) for other image formats
# free from [url]http://www.pythonware.com/products/pil/index.htm[/url]
# give tkinter a namespace to avoid conflicts with PIL
# (they both have a class named Image)

import tkinter as tk
from PIL import Image, ImageTk
from tkinter.ttk import Frame, Button, Style
import time
import glob
import os

def get_latest_image():
    while 1:
        list_of_files = glob.glob('*.bmp')
        if list_of_files:
            break
        time.sleep(0.1)
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

def update_image(panel1, root, latest_image, current_image):
    imageFile = get_latest_image()
    if imageFile != current_image:
        current_image = imageFile
        readok = False
        while not readok:
            try: 
                latest_image = ImageTk.PhotoImage(Image.open(imageFile))
                readok = True
            except:
                readok = False
                pass
        print("Display %s" % imageFile)
    panel1.configure(image=latest_image)
    panel1.image = latest_image
    root.after(100, update_image,panel1,root,latest_image,current_image)       # Set to call again in 30 seconds

def main():
    root = tk.Tk()
    root.title('My Pictures')

    # pick an image file you have .bmp  .jpg  .gif.  .png
    # load the file and covert it to a Tkinter image object
    imageFile = get_latest_image()
    current_image = imageFile
    print("Will display %s" % current_image)
    latest_image = ImageTk.PhotoImage(Image.open(imageFile))

    # get the image size
    w = latest_image.width()
    h = latest_image.height()

    # position coordinates of root 'upper left corner'
    x = 0
    y = 0

    # make the root window the size of the image
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))

    # root has no image argument, so use a label as a panel
    panel1 = tk.Label(root, image=latest_image)
    panel1.image = latest_image
    panel1.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
    panel1.configure(image=latest_image)

    print("Starting to display %s" % imageFile)
    root.after(100, update_image, panel1, root, latest_image, current_image)
    root.mainloop()

if __name__ == '__main__':
    main()
