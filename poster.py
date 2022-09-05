from cProfile import label
from re import X
import tkinter as tk
from tkinter import Button, Label, Place, filedialog, Text
import os
import subprocess
import pyautogui
import time
import webbrowser
import codecs




root=tk.Tk()
root.configure(background="#263D42")
root.title("El-Time FB poster")
root.iconbitmap("D:/Job/facebookposter/elico.ico")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width)
print(screen_height)
root.geometry(f'{screen_width-200}x{screen_height-200}')
root.resizable(False,False)

ffp=""
fileName=""
filePath=""
lineCounter=0
stcounter=0
#root.geometry=('1680x1080')
canvas=tk.Canvas(root, height=20, width=300,bg="red")
def nextStep():
    global stcounter
    if stcounter==0:
        grtngs.pack_forget()
        step1.pack()
        inputxt.pack()
        display.pack()
        
        stcounter=stcounter+1
    else:
        if stcounter==1:
            step1.pack_forget()
            inputxt.pack_forget()
            display.pack_forget()
            step2.pack()
            canvas.pack()
            openFile.pack()
            hint2.pack()
            hint2a.pack()
            stcounter=stcounter+1
            prbtn.pack(side=tk.LEFT)
        else:
            if stcounter==2:
                step2.pack_forget()
                canvas.pack_forget()
                openFile.pack_forget()
                nsbtn.pack_forget()
                step3.pack()
                startScript.pack()
                atnt.pack()
                hint2.pack_forget()
                hint2a.pack_forget()

def prevStep():
    global stcounter
    if stcounter==2:
        step3.pack_forget()
        startScript.pack_forget()
        atnt.pack_forget()
        step2.pack()
        canvas.pack()
        openFile.pack()
        hint2.pack()
        hint2a.pack()
        stcounter=stcounter-1
        nsbtn.pack(side=tk.RIGHT)
    else:
        if stcounter==1:
            step2.pack_forget()
            canvas.pack_forget()
            openFile.pack_forget()
            step1.pack()
            inputxt.pack()
            display.pack()
            hint2.pack_forget()
            hint2a.pack_forget()
            #stcounter=stcounter-1
            prbtn.pack_forget()
        
    



def takeInput():
    input=inputxt.get("1.0","end-1c")
    f=codecs.open('D:/Job/facebookposter/description.txt','w','utf-8')
    f.writelines(input)
    f.close()
    f=open('D:/Job/facebookposter/description.txt','r')
    global lineCounter
    lineCounter=len(f.readlines())
    print(lineCounter)
    
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
    global filePath
    filePath=ffp[0:sl]
    print(filePath)
    global fileName
    fileName=ffp[sl+1:]
    print(fileName)
    
    

#l=Label(text="Fill field with text", bg="#263D42")
inputxt=Text(root, height=40,width=150,fg="white",bg="black",insertbackground="white")
display= Button(root, height=2,width=20,text="Save Content", fg='#263D42', bg="red", command=lambda:takeInput())
openFile = tk.Button(master=root, text="Open File", padx=25,
                     pady=10, fg='#263D42', bg="red", command=addApp)

grtngs=Label(text="Добро подаловать в El-Time FaceBook Poster")
step1=Label(text="Введите текст который будет в Вашей публикации")
step2=Label(text="Выберите файл который будет изображением в Вашей публикации")
hint2=Label(text="Данный этап можно пропустить")
hint2a=Label(text="ВНИМАНИЕ:Путь к файлу не может содержать буквы неанглийского алфавита!!!")
step3=Label(text="Для запуска Бота нажмите на кнопку Start")
atnt=Label(text="ПЕРЕД ЗАПУСКОМ УБЕДИТЕСЬ ЧТО У ВАС АНГЛИЙСКАЯ(ИЛИ ПОЛЬСКАЯ) РАСКЛАДКА КЛАВИАТУРЫ!!!")
grtngs.pack()


#display.place(x=960,y=855)
#l.pack()


nsbtn = tk.Button(master=root, text="Далее", padx=25,
                     pady=10, fg='#263D42', bg="red", command=nextStep)
                    
prbtn=tk.Button(master=root, text="Назад", padx=25,
                    pady=10, fg='#263D42', bg="red",command=prevStep)

nsbtn.pack(side=tk.RIGHT)



#An array with groups IDs


groups =['455531398260426',
'dopomogagansk','1047364845298986','4992908560835432',
# '2871528866309227', Regulamin acception
'2739552006257224','2598819683692207','rabotavgdanske','2538906369688250','2507673389493222','2366497550342111','2269054789981675','LegalWorkEurope','1993337274281752','work.business.travel.group','1978984955669389','1949438151964953','1900974393307349','1873128166260042','1Work.Europe1','rabota.in.Poland','1571981592851440','1529158570561057','1499120036820114','1485180821545842','1365715353597082','1350814111769050','1245694692911126','1128197457535369','1074260426360433','1068946813236033','1059162747874715','rabota.dla.svarshikov','1040691996264992','gdansk.praca.dla.ciebie','922796741194367','898608454048974','861952327536486','poland2024','workpl','824308357719884','823376301523388','822340908260658','820655731395142','Rabota.Typical.Poznan','810637929293329','795707517166288','795227264655678','KalininGradRus','742419679422983','Bydgoszcz.Torun','714615522028505',
#'ilovekharkiv', Publication is not allowed
'658635574480894','ivisiblehelp.ogloszenia.bydgoszcz','worke2019','599337480926745','apoznan','577128642621514','545863903352940','533695340996240','512919872558292','507427714042874','BBSWOI','494253680951740','488680901488862','446242090250869','433405130566394','wgpi.eu','PracaWPoslce','ASP.pl.Praca','400163897113751','383347379180490','378518595974611','370819890094752','362971971008326','344246356398965','329203817738426','325118111355525','315788006179927','313719172644265','311550582779890','309831246329984','299196500420514','294934594291442','ivisiblehelp.ogloszenia.poznan','269511946819724','264448957510473','253384668349682','ivisiblehelp.ogloszenia.lodz','typical.poznan','belarusywbelsko','praca.polska1','wkpoland','WrocLove24','Pracadefo','PracaDlaUkraincowZG','200790123702652','199143564291110','198473674006268','ivisiblehelp.ogloszenia.gdansk','191172435107057','steelfixer','httpswww.instagram.comheadwayconsultingspzoo','180859215974333','177327256978437','169117093491479','ua2pl','154979215211739','150848443518632','nashivpolshe','jobgdansk','141751815872015','136270500355508','133662607366719'
]


def mainScript():
        global filePath
        global fileName
        time.sleep(3)
        #Open a file with the text for the post a copying the content 
        #os.system("notepad description.txt")
        webbrowser.open("D:/Job/facebookposter/description.txt")
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
        for i in range(len(groups)):
            link="https://www.facebook.com/groups/"+groups[i]
            pyautogui.typewrite(link)
            pyautogui.typewrite('\n')
            time.sleep(15)
            #Opening postCreator
            #for j in range(tb):
            #    pyautogui.typewrite("\t")
            #pyautogui.typewrite("\n")
            #pyautogui.keyDown('ctrl')
            #pyautogui.typewrite('f')
            pyautogui.click(540,225)

            time.sleep(6)
            #Filling field with content
            pyautogui.hotkey('ctrl','v')
            time.sleep(4)
            x=870
            y=680
            if lineCounter>=12:
                x=870
                y=810
            else:
                if lineCounter<=3:
                    x=870
                    y=680
                else:
                    if lineCounter<=5:
                        for j in range (lineCounter-3):
                            y=y+23
                        else:
                            if lineCounter==6:
                                y=726
                            else:
                                if lineCounter<=11 and lineCounter>=7:
                                    y=726
                                    for j in range (lineCounter-5):
                                        y=y+10
            #Opening window for file attach
            #for j in range(3):
            #    pyautogui.typewrite("\t")
            #pyautogui.typewrite("\n")
            pyautogui.click(870,810)
            time.sleep(3)
            if fileName!="":
                pyautogui.typewrite(fileName)
                for j in range(5):
                    pyautogui.typewrite("\t")
                time.sleep(4)
                pyautogui.typewrite("\n")
                pyautogui.typewrite(filePath)
                pyautogui.typewrite("\n")
                time.sleep(2)
                #for j in range(10):
                #    pyautogui.typewrite("\t")
                time.sleep(2)
                pyautogui.click(770,810)
            time.sleep(2)
            #for j in range(4):
            #   pyautogui.typewrite("\t")
            pyautogui.click(870,875)
            time.sleep(2)
            #pyautogui.typewrite("\t")
            #pyautogui.typewrite("\n")
            time.sleep(15)
            pyautogui.write(['f4'])
            time.sleep(1)
startScript=tk.Button(root, text="Start", fg='#263D42', bg="red", command=mainScript, height=10, width=40,font=("Arial",25))

root.mainloop()