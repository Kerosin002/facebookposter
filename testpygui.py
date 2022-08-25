import os
import tkinter as tk
from tkinter import Button, Label,Text
from tkinter import filedialog

root=tk.Tk()

ffp=""
fileName=""
filePath=""
root.geometry=('1680x1080')
canvas=tk.Canvas(root, height=20, width=300,bg="blue")

def takeInput():
    input=inputxt.get("1.0","end-1c")
    f=open('description.txt','w')
    f.writelines(input)
    f.close()
    print(input)

def addApp():
    for widget in canvas.winfo_children():
        widget.destroy()
    ffp=filedialog.askopenfilename(
        initialdir="/",title="Select File"
    )
    print(ffp)
    sl=ffp.rfind('/')
    label = tk.Label(canvas, text=ffp, bg="gray")
    label.pack()
    filePath=ffp[0:sl]
    print(filePath)
    fileName=ffp[sl+1:]
    print(fileName)

l=Label(text="Fill field with text")
inputxt=Text(root, height=40,width=150)
display= Button(root, height=2,width=20,text="Save Content", command=lambda:takeInput())
openFile = tk.Button(root, text="Open File", padx=25,
                     pady=10, fg='white', bg="#263D42", command=addApp)
l.pack()
inputxt.pack()
canvas.pack()
openFile.pack()
display.pack()



root.mainloop()