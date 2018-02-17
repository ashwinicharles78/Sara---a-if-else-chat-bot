import KMP_algorithm
from datetime import *
import time
import speech_recognition as srg
from gtts import gTTS
from pygame import mixer
import subprocess
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import webbrowser
import cv2

font_large = ("Georgia", 18 )

r = srg.Recognizer()

r.pause_threshold = 0.7
r.energy_threshold = 400

root = Tk()


def camera():
    cap = cv2.VideoCapture(0)
    while(True):
        ret,frame = cap.read()
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
        
def internet():
    subprocess.Popen(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

def date_edit():
    z = datetime.now()
    print("wait a sec....")
    if (int(z.month) == 9):
        tts = gTTS(text=("it is %d september two thousand seventeen" %int(z.day)), lang="en-us")
        tts.save("sara.mp3")
        mixer.init()
        mixer.music.load("sara.mp3")
        mixer.music.play()

def rubbish():
    tts = gTTS(text="if you don't know the full form of this then let me tell you its ", lang="en-us")
    tts.save("sara1.mp3")
    mixer.init()
    mixer.music.load("sara1.mp3")
    mixer.music.play()
    time.sleep(2)
    tts = gTTS(text="Fuck you", lang="en-us")
    tts.save("sara2.mp3")
    mixer.init()
    mixer.music.load("sara2.mp3")
    mixer.music.play()

def shutdown():
    import os
    tts = gTTS(text="bhaad me jaao", lang="hi")
    tts.save("sara3.mp3")
    mixer.init()
    mixer.music.load("sara3.mp3")
    mixer.music.play()
    os.system('shutdown -s')

def search_it(pat):
    variable = ""
    for i in range(11, (len(pat))):
        variable += pat[i]

    print(variable)
    url = "https://www.google.com./search?q={}".format(variable)
    webbrowser.open(url)

def folder_open(pat):
    tts = gTTS(text="In which drive it is", lang="en-us")
    tts.save("sara7.mp3")
    mixer.init()
    mixer.music.load("sara7.mp3")
    mixer.music.play()
    with srg.Microphone() as source:
        print ('In which drive it is.....!!!')
        audio = r.listen(source , phrase_time_limit=3)
    pattern1 = r.recognize_google(audio)
    print ('SARA thinks you said:\n' + pattern1)
                        
    tts = gTTS(text="What is the folders name", lang="en-us")
    tts.save("sara8.mp3")
    mixer.init()
    mixer.music.load("sara8.mp3")
    mixer.music.play()
    with srg.Microphone() as source:
        print ('What is the folders name')
        audio = r.listen(source , phrase_time_limit=5)
    pattern2 = r.recognize_google(audio)
    print ('SARA thinks you said:\n' + pattern2)                        
                        
    os.startfile("{}:\{}". format(pattern1 , pattern2))


def search_it2(pat):
    variable = ""
    for i in range(17, (len(pat))):
        variable += pat[i]

    print(variable)
    url = "https://www.youtube.com.tr/search?q={}".format(variable)
    webbrowser.open(url)

def calc():
    subprocess.Popen(r"C:\Windows\System32\calc.exe")

def drive_open(pat):
    subprocess.Popen(r'explorer /select, "%s:\" %pat[5] ')

def judwaa():
    mixer.init()
    mixer.music.load("Judwa.mp3")
    mixer.music.play()    

def Barvis():    
    try :
                    with srg.Microphone() as source:
                        print ('Say something !')
                        audio = r.listen(source , timeout=5 , phrase_time_limit = 4 )
                    pattern = r.recognize_google(audio) #username="ashwinicharles78@gmail.com", password="Cruzofire@7")
                    print ('SARA thinks you said:\n' + pattern)
                    """KMP_algorithm.KMPSearch(r.recognize_google(audio)"""
                    if( KMP_algorithm.KMPSearch(pattern, "Sara open up the browser please Sara Internet please Internet Browser Network Chrome chrome Sara can you get me to internet Sara can you open browser for me")):
                        mixer.init()
                        mixer.music.load("i_can.mp3")
                        mixer.music.play()
                        internet()

                    elif( KMP_algorithm.KMPSearch("date",pattern) or KMP_algorithm.KMPSearch("Date",pattern)):
                        date_edit()

                    elif KMP_algorithm.KMPSearch(pattern,"f you Sara"):
                        rubbish()

                    elif KMP_algorithm.KMPSearch(pattern,"shut up yo shut up Sarah"):
                        shutdown()

                    elif KMP_algorithm.KMPSearch(pattern,"hey Sara how are you doing Sara hey Hey sara Hello Sara hello sala hey sala Hey sala hello sara hey Zara hey zara"):
                        mixer.init()
                        mixer.music.load("sara4.mp3")
                        mixer.music.play()    

                    elif KMP_algorithm.KMPSearch(pattern,"I\'m fine well i am good Sara I am good Sara well i am fine Sara I am fine Sara"):
                        tts = gTTS(text="wow! nice to hear that ", lang="en-us")
                        tts.save("sara5.mp3")
                        mixer.init()
                        mixer.music.load("sara5.mp3")
                        mixer.music.play()

                    elif KMP_algorithm.KMPSearch(("search for"),pattern):
                        mixer.init()
                        mixer.music.load("i_can.mp3")
                        mixer.music.play()
                        search_it(pattern)

                    elif KMP_algorithm.KMPSearch(("Judwaa"),pattern):
                        judwaa()

                    elif KMP_algorithm.KMPSearch("video",pattern):
                        mixer.init()
                        mixer.music.load("sara6.mp3")
                        mixer.music.play()
                        search_it2(pattern)

                    elif KMP_algorithm.KMPSearch("stop",pattern):
                        mixer.music.stop()

                    elif KMP_algorithm.KMPSearch("calculator",pattern):
                        calc()

                    elif KMP_algorithm.KMPSearch("camera",pattern):
                        camera()
                                                
                    elif KMP_algorithm.KMPSearch("drive",pattern):
                        drive_open(pattern)

                    
                    elif  KMP_algorithm.KMPSearch("folder",pattern):
                        folder_open(pattern)

                    elif KMP_algorithm.KMPSearch(pattern,"Sara can you predict my future Sara can u predict my future Sara can you see my future Sara can you tell me scope in engineeringSara can you tell my scope in engineering what is my future Sara is my future bright"):
                        image = Image.open("bell.jpg")
                        image.show()
                        
                    elif KMP_algorithm.KMPSearch(pattern,"Sara I love you Sara"):
                        tts = gTTS(text="I have a boyfriend and his name is Jay Cuttler")
                        tts.save("sara9.mp3")
                        mixer.init()
                        mixer.music.load("sara9.mp3")
                        mixer.music.play()
                        search_it("search for Jay Cutler")

                    else:
                        mixer.init()
                        mixer.music.load("A wire.mp3")
                        mixer.music.play(start=19.5)
                    
    except LookupError:
                    print("Could not understand audio")

def Barvis_gui():
        
    lab = Label(root , text = "Hey yo I am SARA how can i help you. \nJust press the mic button and speak into it or get lost by clicking on exit button" , font = font_large )
    lab .pack()
    b2 = ttk.Button(root , text = "Exit" , command = quit).pack(side = "left",padx = 10 , pady = 10)
    b1 =ttk.Button(root, text = None , command=Barvis )
    photo = ImageTk.PhotoImage(file = "images.png")
    b1.config(image = photo )
    b1.image = photo
    b1.pack(side="right", padx=10, pady=10)


Barvis_gui()
"""
if __name__== " __main__":
    pass
else:
    while(1):
        Barvis()
"""
root.mainloop()
