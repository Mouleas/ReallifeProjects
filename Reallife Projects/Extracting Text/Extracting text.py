import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import pytesseract
from PIL import Image
'''
	tkinter is a python gui module which is used to create gui based dialog boxes
	Use this command in cmd "pip install tkinter" to intall tkinter
	Pytesseract is a another module which is used to read the text in the image
	Use this command in cmd "pip install pytesseract" to install pytesseract
	Make sure to download tesseract-ocr from internet and paste the location of the app
'''
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\M0u1ea5\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# In this function we read the text presented in the image

def readTxt():
	fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetype=(("ALL Files","*.*"),("PNG File","*.png"),\
		("JPEG File","*.jpeg")))
	t1.set(fln)
	txt2.delete("1.0","end")
	txt2.insert(INSERT,pytesseract.image_to_string(Image.open(fln)))

# Here we initialise the tkinter module
root = Tk()

# This is a function wihch is presented in the pytesseract module documentation
t1 = StringVar()

# Here we specify the button (width and height) and display board (width and height)
wrapper = LabelFrame(root,text = "Choose File")
wrapper.pack(fill = "both",expand = "yes",padx =10 ,pady = 10)

wrapper2 = LabelFrame(root,text = "Image Text")
wrapper2.pack(fill = "both",expand = "yes",padx = 10 ,pady = 10)

txt = Entry(wrapper,textvariable = t1)
txt.pack(side=tk.LEFT,padx = 10,pady=10)

btn = Button(wrapper,text = "Browse",command = readTxt)
btn.pack(side = tk.LEFT,padx = 10,pady=10)

txt2 = Text(wrapper2)
txt2.pack(padx=10,pady=10)

width = "400"
height = "400"

Title = "Image reader"

# Here we specify the dialog box height and width
root.geometry(f"{width}x{height}")

# Here we specify the title of the dialog box
root.title(f"{Title}")

# If you want to resize the dialog box make sure to type True
root.resizable(False,False)

root.mainloop()