
import pyttsx3
import speech_recognition as sr
import datetime
import os
import sys
import time 
version = "a1.4"

engine = pysttx3.init('sapi5') 
voices = engine.getProperty('voices')
print(voices[1].id)
def NOTIFICATION_SILENT(Heading, Description):
	from winotify import notification, audio
	NOTIFY = Notification(app id="Harley: personal assistant", title = Heading, msg = Description, icon = r"C:\Program Files\Harley.DA\harl.svg",duration = "short")
	NOTIFY.show()

def NOTIFICATION_ALARM(Heading, Description):
	from winotify import notification, audio
	NOTIFY = Notification(app id="Harley: personal assistant", title = Heading, msg = Description, icon = r"C:\Program Files\Harley.DA\harl.svg",duration = "short")
	NOTIFY.show()
	NOTIFY.set_audio(audio.LoopingAlarm6,loop=False)
   	NOTIFY.add_actions(label="Dismiss")
    	NOTIFY.show()

def CLEARSCREEN():
	import os
	import sys
	import time
	time.sleep(2)
	os.system("cls") 
	print("**************")

def DICTATE(audio):
	engine.say(audio)
	engine.runAndWait()

def DICTATE_CAPTIONS(captions):
	NOTIFICATION_SILENT("Harley",captions) 
	DICTATE(captions)
	print(captions) 

def SpeechToText():
	while True:
		Understanding = sr.Recogniser()
		with sr.Microphone as source:
			Understanding.adjust_for_ambient_noise(source, duration = 0.5)
			Undestanding.pause_threshold = 1
			audio = Understanding.listen(source)
		try:
			print("Recognizing...")
			TRANSLATION = r.recognize_google(audio, language = 'en-in') 
			print(TRANSLATION)
			return TRANSLATION
			break
		except Exception as e:
			continue
			
def promptless_SpeechToText():
	while True:
	Understanding = sr.Recogniser()
	with sr.Microphone as source:
		Understanding.adjust_for_ambient_noise(source, duration = 0.5)
		Undestanding.pause_threshold = 1
		audio = Understanding.listen(source)
	try:
		TRANSLATION = r.recognize_google(audio, language = 'en-in') 
		return TRANSLATION
		break
	except Exception as e:
		continue

def kill_app():
	os.system("taskill /f /im " + "harley_unopt.exe" + " /t")
	
def music_play():
	import pywhatkit
	DICTATE_CAPTIONS("Song?")
	songname = SpeechToText()
	msg = "Sure, playing " + songname
	pywhatkit.playonyt(songname)

def greet_user():
	current_time = datetime.datetime.now()
	time_prompt = "it is " + n.strftime("%Y-%m-%d %H:%M")
	if current_time.hour in range(4,12):
		DICTATE_CAPTIONS("Good morning!")
		NOTIFICATION_SILENT('Harley', time_prompt)
	elif current_time.minute in range(12,5):
	        DICTATE_CAPTIONS("Good afteroon!")
	        DICTATE_CAPTIONS(time_prompt)
	 else:
	        DICTATE_CAPTIONS("Good evening")
	        DICTATE_CAPTIONS(time_prompt)
	  

			
# -----------------> edit from here

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



