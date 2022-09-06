from cgitb import text
from logging import root
from threading import Timer

import tkinter as tk
from tkinter import Button, Frame, Label, Place, Toplevel, filedialog, Text


from pynput.mouse import Listener
counter=0
def on_click(x,y,button,pressed):
      if pressed:
         print("Mouse clicked at ({0},{1} with {2})".format(x,y,button))
def clicker():
   with Listener(on_click=on_click) as listener:
      Timer(5, listener.stop).start()
      global counter
      counter=counter+1
      global step
      if counter==1:
         step.config(text="Отметьте точку для отправки поста")
      if counter==2:
         step.config(text="Отметьте точку для отправки поста\n при максимальном размере\n поля ввода")
      print(counter)
      listener.join()

root=tk.Tk()
root.configure(background="#263D42")
root.title("El-Time FB poster CooSetup")
root.iconbitmap("D:/Job/facebookposter/elico.ico")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width)
print(screen_height)
root.geometry(f"200x200+0+{screen_height-300}")
root.resizable(False,False)
root.wm_attributes("-topmost",True)

storeCoo = tk.Button(master=root, text="Отметить", padx=25,
                     pady=10, fg='#263D42', bg="red", command=clicker)
step=Label(master=root,text="Отметьте точку для создания поста")
step.pack()
storeCoo.pack()
root.mainloop()