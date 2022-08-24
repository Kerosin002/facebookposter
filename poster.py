import tkinter as tk
from tkinter import filedialog, Text
import os
import subprocess
import pyautogui
import time
import webbrowser
import codecs

root=tk.Tk()
filePath=""
fileName=""
ffp=""

#An array with groups IDs
print ("Choose the workmode")
print ("1:Normal")
print ("2:Testing")
workMode=input()
if workMode=='1':
    tb=21
if workMode=='2':
    tb=48
groups =['5174877652560467','5174877652560467','5174877652560467','5174877652560467','5174877652560467']
os.chdir("D:/Job/facebookposter")
print("Shall Your post has an attached file?\n1:For yes\n2:For No ")
answer=input()


time.sleep(3)
if answer=='1':
    print("Please, paste a path to the file")
    filePath=input()
    print("Now please write down a file name(for example pic.jpg)")
    fileName=input()
#Open a file with the text for the post a copying the content 
#os.system("notepad description.txt")
webbrowser.open("description.txt")
time.sleep(2)
pyautogui.keyDown('ctrl')
pyautogui.typewrite('a')
time.sleep(1)
pyautogui.typewrite('c')
pyautogui.keyUp('ctrl')
#Opening a webBrowser
subprocess.Popen(["C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"])




time.sleep(5)
#In Browser opening a new tab
pyautogui.keyDown('ctrl')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('ctrl')
#Loop for post only with text
if answer=='2':
    for i in range(len(groups)):
        link="https://www.facebook.com/groups/"+groups[i]
        pyautogui.typewrite(link)
        pyautogui.typewrite('\n')
        time.sleep(10)
        for j in range(tb):
            pyautogui.typewrite("\t")
        pyautogui.typewrite("\n")
        time.sleep(3)
        pyautogui.hotkey('ctrl','v')

        time.sleep(3)
        for j in range(9):
            pyautogui.typewrite("\t")
        pyautogui.typewrite("\n")
        time.sleep(3)
        pyautogui.write(['f4'])
        time.sleep(1)
if answer=='1':
    for i in range(len(groups)):
        link="https://www.facebook.com/groups/"+groups[i]
        pyautogui.typewrite(link)
        pyautogui.typewrite('\n')
        time.sleep(10)
        #Opening postCreator
        for j in range(tb):
            pyautogui.typewrite("\t")
        pyautogui.typewrite("\n")
        #pyautogui.keyDown('ctrl')
        #pyautogui.typewrite('f')

        time.sleep(2)
        #Filling field with content
        pyautogui.hotkey('ctrl','v')
        #Opening window for file attach
        for j in range(4):
            pyautogui.typewrite("\t")
        pyautogui.typewrite("\n")
        time.sleep(2)
        pyautogui.typewrite(fileName)
        for j in range(5):
            pyautogui.typewrite("\t")
        time.sleep(2)
        pyautogui.typewrite("\n")
        pyautogui.typewrite(filePath)
        pyautogui.typewrite("\n")
        time.sleep(2)
        for j in range(10):
            pyautogui.typewrite("\t")
        time.sleep(2)
        pyautogui.typewrite("\n")
        for j in range(4):
            pyautogui.typewrite("\t")
        time.sleep(2)
        pyautogui.typewrite("\t")
        pyautogui.typewrite("\n")
        time.sleep(10)
        pyautogui.write(['f4'])
        time.sleep(1)