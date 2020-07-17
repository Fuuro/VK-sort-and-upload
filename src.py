import vk_api
import time
import json
import requests
import sys
import random
from vk_api import VkUpload
import os 
import tkinter as tk
from tkinter import Frame, Tk, Button
from PIL import ImageTk, Image
import shutil 
import glob
from os import listdir
from os.path import isfile, join
import re

f = open("D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/pics.txt", "r",encoding='utf-8-sig')
pics = f.readlines()
f.close()
f = open("D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/10.txt", "r",encoding='utf-8-sig')
tentxt = f.readlines()
f.close()
tentxt = [item.strip() for item in tentxt]
f = open("D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/7.txt", "r",encoding='utf-8-sig')
seventxt = f.readlines()
f.close()
seventxt = [item.strip() for item in seventxt]
f = open("D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/5.txt", "r",encoding='utf-8-sig')
fivetxt = f.readlines()
f.close()
fivetxt = [item.strip() for item in fivetxt]
f = open("D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/1.txt", "r",encoding='utf-8-sig')
onetxt = f.readlines()
f.close()
onetxt = [item.strip() for item in onetxt]
def redraw():
        path = pics[0]
        img = Image.open(path)
        size = 900,900
        img.thumbnail(size, Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        
        panel.configure(image=img)
        panel.image = img # keep a reference!
def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device
def captcha_handler(captcha):
    """ При возникновении капчи вызывается эта функция и ей передается объект
        капчи. Через метод get_url можно получить ссылку на изображение.
        Через метод try_again можно попытаться отправить запрос с кодом капчи
    """

    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)    
def post():
    os.chdir("D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/")
    login, password = '', '' 
    vk_session = vk_api.VkApi(login,password,auth_handler=auth_handler,captcha_handler=captcha_handler )   
    vk_session.auth()
    vk = vk_session.get_api()
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    owner_id = '' #id группы или владельца  писать с минусом
     
    if not tentxt:
        if not seventxt:
            if not fivetxt:
                if not onetxt:
                    print("all lists is empty")
                    return
                else: filteredpics=onetxt
            else: filteredpics=fivetxt
        else: filteredpics=seventxt 
    else: filteredpics=tentxt
    import re
    o=filteredpics[0]
    o=o.replace("\\", "/")
    o=o.split('/')
    o=o[-1]
    match = re.match(r"^(.+)(\_[^_]+){2}$", o)
    o=" "
    if match:
        o=match.group(1) 
        
        
    
    

   
    upload = vk_api.VkUpload(vk_session)

    photo = upload.photo_wall( filteredpics[0],  group_id=,caption=o) #добавить свой id группы
    attachment = ','.join('photo{owner_id}_{id},'.format(**item) for item in photo)
    vk_photo_url = 'https://vk.com/photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id'])

    print(photo, '\nLink: ', vk_photo_url)
    
    vk_session.method("wall.post",{
             'owner_id' : owner_id,
             'message': "   ",   
             'attachments': attachment,
             "from_group" : "1"
             
        })
    if tentxt==filteredpics:
        
        dest = shutil.move(filteredpics[0], destination)
        tentxt.remove(tentxt[0])
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/10.txt', 'w',encoding='utf-8-sig') as f:
            for item in tentxt:
                f.write("%s\n" % item)
    if seventxt==filteredpics:
        
        dest = shutil.move(filteredpics[0], destination)
        seventxt.remove(seventxt[0])
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/7.txt', 'w',encoding='utf-8-sig') as f:
            for item in seventxt:
                f.write("%s\n" % item)
    if fivetxt==filteredpics:

        dest = shutil.move(filteredpics[0], destination)
        fivetxt.remove(fivetxt[0])
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/5.txt', 'w',encoding='utf-8-sig') as f:
            for item in fivetxt:
                f.write("%s\n" % item)
    if onetxt==filteredpics:

        dest = shutil.move(filteredpics[0], destination)
        onetxt.remove(onetxt[0])
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/1.txt', 'w',encoding='utf-8-sig') as f:
            for item in onetxt:
                f.write("%s\n" % item)
utime=time.time()
utime=utime/1
def timepost():
    os.chdir("D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/")
    login, password = '', ''
    vk_session = vk_api.VkApi(login,password,auth_handler=auth_handler,captcha_handler=captcha_handler )   
    vk_session.auth()
    vk = vk_session.get_api()
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    owner_id = '' #id группы или владельца  писать с минусом
    if not tentxt:
        if not seventxt:
            if not fivetxt:
                if not onetxt:
                    print("all lists is empty")
                    return
                else: filteredpics=onetxt
            else: filteredpics=fivetxt
        else: filteredpics=seventxt 
    else: filteredpics=tentxt
    global utime

    o=filteredpics[0]
    o=o.replace("\\", "/")
    o=o.split('/')
    o=o[-1]
    match = re.match(r"^(.+)(\_[^_]+){2}$", o)
    o=" "
    if match:
        o=match.group(1) 
   
    upload = vk_api.VkUpload(vk_session)

    photo = upload.photo_wall( filteredpics[0],  group_id=,caption=o) #добавить свой id группы
    attachment = ','.join('photo{owner_id}_{id},'.format(**item) for item in photo)
    vk_photo_url = 'https://vk.com/photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id'])

    print(photo, '\nLink: ', vk_photo_url)
    
    vk_session.method("wall.post",{
             'owner_id' : owner_id,
             'message': "    ",   
             'attachments': attachment,
             "from_group" : "1",
             'publish_date' : int(utime)+3600
             
        })
    utime+=3600
    if tentxt==filteredpics:
        
        dest = shutil.move(filteredpics[0], destination)
        tentxt.remove(tentxt[0])
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/10.txt', 'w',encoding='utf-8-sig') as f:
            for item in tentxt:
                f.write("%s\n" % item)
    if seventxt==filteredpics:
        
        dest = shutil.move(filteredpics[0], destination)
        seventxt.remove(seventxt[0])
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/7.txt', 'w',encoding='utf-8-sig') as f:
            for item in seventxt:
                f.write("%s\n" % item)
    if fivetxt==filteredpics:

        dest = shutil.move(filteredpics[0], destination)
        fivetxt.remove(fivetxt[0])
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/5.txt', 'w',encoding='utf-8-sig') as f:
            for item in fivetxt:
                f.write("%s\n" % item)
    if onetxt==filteredpics:

        dest = shutil.move(filteredpics[0], destination)
        onetxt.remove(onetxt[0])
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/1.txt', 'w',encoding='utf-8-sig') as f:
            for item in onetxt:
                f.write("%s\n" % item)
def timepost25():
    for pepe in range(3):
      timepost()
count=0
path = 'D:/ы/!!!!!!!!!!!!!!!!/pictures/'

# файл который нужно перенести


    # куда перенести
pics = [item.strip() for item in pics]

if os.listdir('C:/Users/Admin/Downloads/twitterimage/'): #если есть файлы в адсадсадс
    os.chdir("C:/Users/Admin/Downloads/twitterimage/")
    asdasdpics = [f for f in os.listdir('.') if os.path.isfile(f) and os.path.splitext(f)[1] != ".json" and os.path.splitext(f)[1] != ".mp4" and os.path.splitext(f)[1] != ".gif"]
    asdasdpics.sort(key = lambda x: os.path.getmtime(x))
    asdfgh=asdasdpics
    string2="C:/Users/Admin/Downloads/twitterimage/"
    asdfgh=[string2 + x for x in asdfgh]
    string='D:/ы/!!!!!!!!!!!!!!!!/pictures/'
    asdasdpics = [string + x for x in asdasdpics]
    torture=len(asdasdpics)
    for k in range(0,torture):
        check_existence = os.path.join(string, os.path.basename(asdfgh[0]))
        if os.path.exists(check_existence):
            os.remove(asdfgh[0])
            asdasdpics.remove(asdasdpics[0])
            asdfgh.remove(asdfgh[0])
        else:
            pics.insert(0, asdasdpics[0])
            asdasdpics.remove(asdasdpics[0])
            asdfgh.remove(asdfgh[0])

    
    

    source = 'C:/Users/Admin/Downloads/twitterimage/' 
    dest1 = 'D:/ы/!!!!!!!!!!!!!!!!/pictures/'

    files = os.listdir(source)

    for f in files:
        shutil.move(source+f, dest1)
    with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/pics.txt', 'w',encoding='utf-8-sig') as f:
            for item in pics:
                f.write("%s\n" % item)
    
destination = 'D:/ы/!!!!!!!!!!!!!!!!/pictures/o1'
#интерфейс
def ten(panel):
    check_existence = os.path.join(destination, os.path.basename(pics[0]))
    if os.path.exists(check_existence):
        os.remove(pics[0])
        pics.remove(pics[0])
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/pics.txt', 'w',encoding='utf-8-sig') as f:
            for item in pics:
                f.write("%s\n" % item)
        redraw()      
    else:
        
        tentxt.insert(0,pics[0])
        pics.remove(pics[0])
        redraw()
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/pics.txt', 'w',encoding='utf-8-sig') as f:
            for item in pics:
                f.write("%s\n" % item)
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/10.txt', 'w',encoding='utf-8-sig') as f:
            for item in tentxt:
                f.write("%s\n" % item)
    return tentxt
def seven(panel):
    check_existence = os.path.join(destination, os.path.basename(pics[0]))
    if os.path.exists(check_existence):
        os.remove(pics[0])
        pics.remove(pics[0])
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/pics.txt', 'w',encoding='utf-8-sig') as f:
            for item in pics:
                f.write("%s\n" % item)
        redraw()    
    else:
        
        seventxt.insert(0,pics[0])
        pics.remove(pics[0])
        redraw()
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/pics.txt', 'w',encoding='utf-8-sig') as f:
            for item in pics:
                f.write("%s\n" % item)
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/7.txt', 'w',encoding='utf-8-sig') as f:
            for item in seventxt:
                f.write("%s\n" % item)
    return seventxt  
def five(panel):
    check_existence = os.path.join(destination, os.path.basename(pics[0]))
    if os.path.exists(check_existence):
        os.remove(pics[0])
        pics.remove(pics[0])
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/pics.txt', 'w',encoding='utf-8-sig') as f:
            for item in pics:
                f.write("%s\n" % item)
        redraw()       
    else:
        
        fivetxt.insert(0,pics[0])
        pics.remove(pics[0])
        redraw()
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/pics.txt', 'w',encoding='utf-8-sig') as f:
            for item in pics:
                f.write("%s\n" % item)
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/5.txt', 'w',encoding='utf-8-sig') as f:
            for item in fivetxt:
                f.write("%s\n" % item)
    return fivetxt

def one(panel):
    check_existence = os.path.join(destination, os.path.basename(pics[0]))
    if os.path.exists(check_existence):
        os.remove(pics[0])
        pics.remove(pics[0])
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/pics.txt', 'w',encoding='utf-8-sig') as f:
            for item in pics:
                f.write("%s\n" % item)
        redraw()          
    else:
        
        onetxt.insert(0,pics[0])
        pics.remove(pics[0])
        redraw()
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/pics.txt', 'w',encoding='utf-8-sig') as f:
            for item in pics:
                f.write("%s\n" % item)
        with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/1.txt', 'w',encoding='utf-8-sig') as f:
            for item in onetxt:
                f.write("%s\n" % item)
    return onetxt
def QWERTY(panel):
           
        path = 'D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/'

        # файл который нужно перенести
 

        # куда перенести
        destiny = 'D:/ы/!!!!!!!!!!!!!!!!/pictures/f/newpics'
        check_existence = os.path.join(destiny, os.path.basename(pics[0]))
        if os.path.exists(check_existence):
                os.remove(pics[0])
                pics.remove(pics[0])
                with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/pics.txt', 'w',encoding='utf-8-sig') as f:
                    for item in pics:
                        f.write("%s\n" % item)
                redraw()     
        else:
                dest = shutil.move(pics[0], destiny)
                pics.remove(pics[0])
                redraw()
                with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/pics.txt', 'w',encoding='utf-8-sig') as f:
                    for item in pics:
                        f.write("%s\n" % item)
def DELET(panel):
           
        path = 'D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/'

        # файл который нужно перенести
 

        # куда перенести
        destiny = 'D:/ы/!!!!!!!!!!!!!!!!/pictures/f/'
        check_existence = os.path.join(destiny, os.path.basename(pics[0]))
        if os.path.exists(check_existence):
                os.remove(pics[0])
                pics.remove(pics[0])
                with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/pics.txt', 'w',encoding='utf-8-sig') as f:
                    for item in pics:
                        f.write("%s\n" % item)
                redraw()       
        else:
                os.remove(pics[0])
                pics.remove(pics[0])
                redraw()
                with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/pics.txt', 'w',encoding='utf-8-sig') as f:
                    for item in pics:
                        f.write("%s\n" % item)
def stuff(panel):
           
        path = 'D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/'

        # файл который нужно перенести
 

        # куда перенести
        destiny = 'D:/ы/!!!!!!!!!!!!!!!!/pictures/2+stuff/'
        check_existence = os.path.join(destiny, os.path.basename(pics[0]))
        if os.path.exists(check_existence):
                os.remove(pics[0])
                pics.remove(pics[0])
                with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/pics.txt', 'w',encoding='utf-8-sig') as f:
                    for item in pics:
                        f.write("%s\n" % item)
                redraw()     
        else:
                dest = shutil.move(pics[0], destiny)
                pics.remove(pics[0])
                redraw()
                with open('D:/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/pics.txt', 'w',encoding='utf-8-sig') as f:
                    for item in pics:
                        f.write("%s\n" % item)
#Create main window
window = Tk()


#divide window into two sections. One for image. One for buttons
bottom = tk.Frame(window)
bottom.pack(side="bottom")

#place image
path = pics[0]
img = Image.open(path)
size = 1000,900
img.thumbnail(size, Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = tk.Label(window, image = img)
panel.image = img # keep a reference!
panel.pack(side = "top", fill = "both", expand = "no")


#place buttons
next_button = tk.Button(window, text="10", width=10, height=2, command=lambda: ten(panel))
next_button.pack(in_=bottom, side="right")  
next_button = tk.Button(window, text="7.5", width=10, height=2, command=lambda: seven(panel))
next_button.pack(in_=bottom, side="right")
next_button = tk.Button(window, text="5", width=10, height=2, command=lambda: five(panel))
next_button.pack(in_=bottom, side="right")
next_button = tk.Button(window, text="1", width=10, height=2, command=lambda: one(panel))
next_button.pack(in_=bottom, side="right")
next_button = tk.Button(window, text="QWERTY", width=10, height=2, command=lambda: QWERTY(panel))
next_button.pack(in_=bottom, side="right")
next_button = tk.Button(window, text="DELET", width=10, height=2, command=lambda: DELET(panel))
next_button.pack(in_=bottom, side="right")
next_button = tk.Button(window, text="2+stuff", width=10, height=2, command=lambda: stuff(panel))
next_button.pack(in_=bottom, side="right")
next_button = tk.Button(window, text="запостить" + str(len(tentxt)), width=10, height=2, command=lambda: post())
next_button.pack(in_=bottom, side="right")
next_button = tk.Button(window, text="отложка", width=10, height=2, command=lambda: timepost())
next_button.pack(in_=bottom, side="right")
next_button = tk.Button(window, text="отложка3", width=10, height=2, command=lambda: timepost25())
next_button.pack(in_=bottom, side="right")

#Start the GUI
window.mainloop()
#интерфейс^


#if __name__ == '__main__':
 #   main()
    