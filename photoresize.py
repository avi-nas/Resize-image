from turtle import width
from PIL import Image
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

files = filedialog.askopenfilenames()

im = Image.open(files[0])
width = int(input("Enter Width: "))
hight = int(input("Enter Hight: "))
resized_im = im.resize((width,hight))
fileName = input("Enter new file name:")

resized_im.save(fileName+".png")
resized_im.show()





