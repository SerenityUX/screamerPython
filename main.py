from playsound import playsound
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
from captcha.image import ImageCaptcha
import requests
import threading

def printit():
  receiver = "A"
  threading.Timer(0.5, printit).start()
  screams = requests.get(f'https://screamer-disbatch-e167cb5316a6.herokuapp.com/getNewScreams?receiver={receiver}')
  if len(screams.json()["screams"]):
    playsound(f'./{receiver}.mp3')
    print('playing sound using  playsound')
  print(screams.json())
printit()

# Create the main window
parent = tk.Tk()
parent.title("Image in Tkinter")

# Load and display an image 
#(replace 'your_logo.png' with the path to your image file)
image = Image.open('stuff.png')
image = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(parent, image=image)
image_label.pack()

# Start the Tkinter event loop
parent.mainloop()


#main = Tk()
#photo = PhotoImage(file='/Users/hajrahsiddiqui/Documents/hackathon 2024 project /zombie image .webp')
    # Select the Imagename  from a folder 
    # opens the image
#img = Image.open(photo)

    # resize the image and apply a high-quality down sampling filter
#img = img.resize((1000000, 1000000), Image.LANCZOS)
    
#img.show() 
#main.geometry("1000000x1000000")

    
#main.mainloop()
