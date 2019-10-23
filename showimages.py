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
import sys

class ShowLatestImage():

    def __init__(self):
        self.root = tk.Tk()

        # pick an image file you have .bmp  .jpg  .gif.  .png
        # load the file and covert it to a Tkinter image object
        imageFile = self.getLatestImage()
        self.latestImage = self.readImage(imageFile)
        self.currentImage = imageFile
        self.root.title(imageFile)
        print("Will display %s" % self.currentImage)

        # get the image size
        w = self.latestImage.width()
        h = self.latestImage.height()

        # position coordinates of root 'upper left corner'
        x = 0
        y = 0

        # make the root window the size of the image
        self.root.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # root has no image argument, so use a label as a panel
        self.panel1 = tk.Label(self.root, image=self.latestImage)
        self.panel1.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

        print("Starting to display %s" % imageFile)
        self.root.after(100, self.updateImage)
        self.root.mainloop()

    def readImage(self, imageFile):
        readOk = False
        readCount = 0
        while not readOk:
            try:
                image = ImageTk.PhotoImage(Image.open(imageFile))
                readOk = True
            except:
                readCount = readCount + 1
                if readCount >10:
                    print("Too many file reading failures on %s" % imageFile)
                    sys.exit()
                readOk = False
                time.sleep(0.01)
                pass
        return image


    def getLatestImage(self):
        while 1:
            listOfFiles = glob.glob('*.bmp')
            if listOfFiles:
                break
            time.sleep(0.02)
        latestFile = max(listOfFiles, key=os.path.getctime)
        return latestFile

    def updateImage(self):
        imageFile = self.getLatestImage()
        if imageFile != self.currentImage:
            self.currentImage = imageFile
            self.latestImage = self.readImage(imageFile)
            print("Display %s" % imageFile)
        self.root.title(imageFile)
        self.panel1.configure(image=self.latestImage)
        self.root.after(100, self.updateImage)       # Set to call itself again

def main():
    app = ShowLatestImage()

if __name__ == '__main__':
    main()
