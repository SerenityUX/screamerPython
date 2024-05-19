from playsound import playsound
from tkinter import *
from tkinter import messagebox
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

#python3 -m venv myenv
#source myenv/bin/activate

# for playing note.wav file
#def show():
 #   messagebox.showinfo("Test Popup", "Hello world")
#root = Tk()
#root.title("Main Window")
#root.geometry("500x500")
#toplevel = Toplevel(root)
#toplevel.title("Toplevel Window")
#toplevel.geometry("300x300")
#show_button = Button(root , text = "Show popup" , command = show)
#show_button.place(x = 200 , y = 200)
mainloop()

main = Tk()
photo = PhotoImage(file='/Users/hajrahsiddiqui/Documents/hackathon 2024 project /zombie image .webp')
main.iconphoto()
main.geometry("1000000x1000000")
main.mainloop()

#COME BACK TO WINSOUND THING
#---
#winsound.playsound("zombie.mp3", winsound.SND_ASYNC + winsound.SND_LOOP)
#input("Enter any input to stop sound")
#winsound.playsound(None, 0)
#input("Enter any input to playm sound")
#winsound.PlaySound("zombie.mp3", winsound.SND_ASYNC + winsound.SND_LOOP)
#input("Enter any input to exit")
