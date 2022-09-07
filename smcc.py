from cgitb import text
from itertools import count
from logging import root
from threading import Timer
import configparser
import tkinter as tk
from tkinter import Button, Frame, Label, Place, Toplevel, filedialog, Text
from pynput.mouse import Listener

config=configparser.ConfigParser()
counter=0
config.add_section("coords")
def on_click(x,y,button,pressed):
      global counter
      if pressed:
         print("Mouse clicked at ({0},{1} with {2})".format(x,y,button))
         xs=str(x)
         ys=str(y)
         if counter==1:
            config.set("coords","cx",xs)
            config.set("coords","cy",ys)
         if counter==2:
            config.set("coords","sendx",xs)
            config.set("coords","sendy",ys)
         if counter==3:
            config.set("coords","sendfx",xs)
            config.set("coords","sendfy",ys)
         if counter==4:
            config.set("coords","imgx",xs)
            config.set("coords","imgy",ys)
         if counter==5:
            config.set("coords","opimgx",xs)
            config.set("coords","opimgy",ys)
         with open(r"D:/Job/facebookposter/coords.ini",'w') as configfileObj:
            config.write(configfileObj)
            configfileObj.flush()
            configfileObj.close()
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
      if counter==3:
         step.config(text="Отметьте точку прикрепления\n изображения")
      if counter==4:
         step.config(text="Отметьте точку Открыть\n в окне выбора файла")
      if counter==5:
         step.config(text="Все Готово!\n Можете закрыть окно программы")
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
