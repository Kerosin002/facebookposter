from logging import root
import tkinter as tk
from tkinter import Button, Label, Place, filedialog, Text


from pynput.mouse import Listener

def on_click(x,y,button,pressed):
   if pressed:
      print("Mouse clicked at ({0},{1} with {2})".format(x,y,button))

#with Listener(on_click=on_click) as listener:
#   listener.join()

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
storeCoo = tk.Button(master=root, text="Open File", padx=25,
                     pady=10, fg='#263D42', bg="red", command=on_click)
storeCoo.pack()
root.mainloop()