import os
import subprocess
import pyautogui
import time
import webbrowser
import codecs
#An array with groups IDs
print ("Choose the workmode")
print ("1:Normal")
print ("2:Testing")
workMode=input()
if workMode=='1':
    tb=29
    groups =['455531398260426',
    'dopomogagansk','1047364845298986','4992908560835432',
    # '2871528866309227', Regulamin acception
    '2739552006257224','2598819683692207','rabotavgdanske','2538906369688250','2507673389493222','2366497550342111','2269054789981675','LegalWorkEurope','1993337274281752','work.business.travel.group','1978984955669389','1949438151964953','1900974393307349','1873128166260042','1Work.Europe1','sobytiyadnepr','rabota.in.Poland','1680133438927949','1571981592851440','1529158570561057','1499120036820114','1485180821545842','1473953522915239','1365715353597082','1350814111769050','1245694692911126','1128197457535369','1074260426360433','1068946813236033','1059162747874715','rabota.dla.svarshikov','1040691996264992','gdansk.praca.dla.ciebie','922796741194367','898608454048974','861952327536486','poland2024','workpl','824308357719884','823376301523388','822340908260658','820655731395142','Rabota.Typical.Poznan','810637929293329','795707517166288','795227264655678','KalininGradRus','742419679422983','Bydgoszcz.Torun','714615522028505',
    #'ilovekharkiv', Publication is not allowed
    '658635574480894','ivisiblehelp.ogloszenia.bydgoszcz','worke2019','599337480926745','apoznan','577128642621514','545863903352940','533695340996240','512919872558292','507427714042874','BBSWOI','494253680951740','488680901488862','446242090250869','433405130566394','wgpi.eu','PracaWPoslce','ASP.pl.Praca','400163897113751','383347379180490','378518595974611','370819890094752','362971971008326','344246356398965','329203817738426','325118111355525','315788006179927','313719172644265','311550582779890','309831246329984','299196500420514','294934594291442','ivisiblehelp.ogloszenia.poznan','269511946819724','264448957510473','253384668349682','ivisiblehelp.ogloszenia.lodz','typical.poznan','belarusywbelsko','praca.polska1','wkpoland','WrocLove24','Pracadefo','PracaDlaUkraincowZG','novostixarkova','200790123702652','199143564291110','198473674006268','ivisiblehelp.ogloszenia.gdansk','191172435107057','steelfixer','httpswww.instagram.comheadwayconsultingspzoo','180859215974333','177327256978437','169117093491479','Kharkiw','ua2pl','154979215211739','salebestshop','150848443518632','nashivpolshe','jobgdansk','141751815872015','136270500355508','133662607366719']
if workMode=='2':
    tb=21
    groups =['5174877652560467','5174877652560467','5174877652560467','5174877652560467','5174877652560467']
os.chdir("C:/Users/eltim/facebookposter")
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
        #for j in range(tb):
        #    pyautogui.typewrite("\t")
        #pyautogui.typewrite("\n")
        pyautogui.click(540,225)
        time.sleep(6)
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
        #Opening window for file attach
        #for j in range(3):
        #    pyautogui.typewrite("\t")
        #pyautogui.typewrite("\n")
        pyautogui.click(870,810)
        time.sleep(3)
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
        pyautogui.typewrite("\n")
        time.sleep(10)
        pyautogui.write(['f4'])
        time.sleep(1)