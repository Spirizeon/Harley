'''
█░█ ▄▀█ █▀█ █░░ █▀▀ █▄█   █▀▀ █▀█ █▀█   █░█░█ █ █▄░█ █▀▄ █▀█ █░█░█ █▀
█▀█ █▀█ █▀▄ █▄▄ ██▄ ░█░   █▀░ █▄█ █▀▄   ▀▄▀▄▀ █ █░▀█ █▄▀ █▄█ ▀▄▀▄▀ ▄█
𝒃𝒖𝒊𝒍𝒕 𝒃𝒚 𝑨𝒚𝒖𝒔𝒉; (𝒃𝒓𝒂𝒗𝒐𝒔𝒊𝒄𝒌𝒛@𝒈𝒊𝒕𝒉𝒖𝒃)
'''


import pyttsx3
import speech_recognition as sr
import datetime
import os
import sys
import time 
from tkinter import Menu
import psutil
import pystray
import PIL.Image
import subprocess
version = "a1.4"

    #cpustats = psutil.cpu_percent()
    #ramstats =  psutil.virtual_memory().percent
            


    
        
            
            
            
        
        
            
            
            
            
        ))
    
#MUST BE RUN IN PROGRAM FILES INSIDE THE HARLEY.DA DIRECTORY
engine = pyttsx3.init('sapi5') #microsoft api sapi5
voices = engine.getProperty('voices')
print(voices[1].id) 
engine.setProperty('voice', voices[1].id) #zira voice
def nexrem(big,small):
    from winotify import Notification, audio
    ping = Notification(app_id="Harley: personal assistant",
                        title=big,
                        msg=small,
                        icon = r"C:\Program Files\Harley.DA\harl.svg",
                        duration="short")

    #ping.set_audio(audio.LoopingAlarm6,loop=False)
    ping.show()
def nexremlarm(big,small):
    from winotify import Notification, audio
    ping = Notification(app_id="Harley: personal assistant",
                        title=big,
                        msg=small,
                        icon = r"C:\Program Files\Harley.DA\harl.svg",
                        duration="long")

    ping.set_audio(audio.LoopingAlarm6,loop=False)
    ping.add_actions(label="Dismiss")
    ping.show()
def clearconsol():
    import subprocess
    import os
    import sys
    import time
    time.sleep(2)
    os.system("cls") #clear the console
    print("*****************************")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def preak(s):
    nexrem("Harley",s)
    speak(s)
    print(s)
def ear():
    k = 0
    while k < 1:
        r = sr.Recognizer()
        with sr.Microphone() as source: 
            r.adjust_for_ambient_noise(source, duration=0.5)
            r.pause_threshold = 1 #duration for how long it records
            audio = r.listen(source) #listen
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in') #translate stt
            print(query) #result
            return query
            break
        except Exception as e:
            continue
def glassear(): #ear() but without print functions, good for bg listening
    k = 0
    while k < 1:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1 #duration for how long it records
            audio = r.listen(source) #listen
        try:
            query = r.recognize_google(audio, language='en-in') #translate stt
            return query
            break
        except Exception as e:
            continue
#NOTE: function to kill a running program through cmd input only works for .exe version
def killself():
    os.system("taskkill /f /im "+ "harley_unopt.exe" +" /t")
def woofers():
    import pywhatkit 
    preak("Song?") 
    comm = ear()
    msg = "Sure, playing " + comm 
    preak(msg)
    pywhatkit.playonyt(comm)
def greet():
    n = datetime.datetime.now()
    strmsg = "it is " + n.strftime("%Y-%m-%d %H:%M")
    if n.hour in range(4,12):
        preak("Good morning!")
        nexrem('Harley',strmsg)
    #now.strftime("%Y-%m-%d %H:%M:%S"))
    elif n.minute in range(12,5):
        preak("Good afteroon!")
        preak(strmsg)
    else:
        preak("Good evening")
        preak(strmsg)
def gewgle():
    preak("what do you want to google?")
    y = str(ear())
    import webbrowser as w
    msg = "searching for "+ y
    preak(msg)
    googlink = "https://www.google.com/search?q=" + y.lower()
    w.open_new_tab(googlink)
    clearconsol()
def yewt():
    preak("What do you want to watch?")
    y = str(ear())
    import webbrowser as w
    msg = "searching for "+ y
    preak(msg)
    yewlink = "https://www.youtube.com/results?search_query=" + y.lower()
    w.open_new_tab(yewlink)
    clearconsol()
#user inputs
def alarm():
    preak("Please set your alarm time: ")
    alarmHour = int(input("Hours: "))
    alarmMinute = int(input("Minutes: "))
    nexremlarm("Alarm Setup", "time format?")
    AmPm = input("am/pm : ")

    #12 hour format
    if AmPm == "pm":
        alarmHour += 12
    #confirmation message
    msg = "Alarm set for "+ str(alarmHour) + ":" + str(alarmMinute)
    nexrem("Alarm Setup", msg)

    #setting the alarm
    while True:
        if alarmHour == datetime.datetime.now().hour:
            if alarmMinute == datetime.datetime.now().minute:
                nexrem("Alarm","Your Alarm's ringing!")
                break
def shutdownscript():
    #write a program to shutdown or restart the system on command
    preak("Shutdown or restart?")
    command = str(ear())
    if command == "shutdown":
    
        preak("Shutting down...")
        os.system("shutdown /s /t 1")
    elif command == "restart":
        os.system("shutdown /r /t 1")
        preak("Restarting...")
    else:
        preak("Invalid command")
def reminderlist():
    preak("What do you want to do?")
    command = str(ear())
    if command == "add":
        preak("What do you want to add?")
        reminder = str(ear())
        with open("reminders.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([reminder])
        preak("Reminder added")

    elif command == "show":
        with open("reminders.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                preak(row)


    else:
        preak("Invalid command")



#TEST FROM THIS POINT ---------------->






#starters
greet()
#------------------
speakconst = 0
misc1 = 0

while misc1 < 1:
    clearconsol()
    doccons = 0
    speakgate = glassear() #listens in the background
    
    if 'harley' in speakgate.lower(): #if speech contains harley
        while speakconst < 1: 
            nexrem("Harley","Speak now please...")
            print("Listening...")
            x = ear()
            if "google" in x.lower():
                gewgle()
            elif "alarm" in x.lower(): 
                alarm()
            elif "dev mode" == x.lower():
                nexrem("Harley","Tray released")
                traycon()
            elif "play" in x.lower():
                woofers()
            elif "alarm" in x.lower():
                alarm()
            elif "power off" in x.lower():
                shutdownscript()
            elif x == "close":
                killself()
            elif "thank" in x.lower():
                preak("Glad to be of help")
                break #break 1st while loop
            elif "add a reminder" in x.lower():
                reminderlist()
        
            #clear the console
        continue #back to line 32
    else:
        while doccons < 1:
            nexrem("Harley",'Please call me by my name "Harley" whenever you want my help')
            doccons += 1
        continue
    
        
    #process assignment
    #multiprocessing.Process(target=function name not in strings)



