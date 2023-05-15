
import pyttsx3
import speech_recognition as sr
import datetime
import os
import sys
import time 
#version 1.6

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
	  

			


def gewgle():
    DICTATE_CAPTIONS("what do you want to google?")
    query = str(SpeechToText())
    import webbrowser as w
    srchstring = "searching for "+ query
    DICTATE_CAPTIONS(srchstring)
    googlink = "https://www.google.com/search?q=" + query.lower()
    w.open_new_tab(googlink)
    CLEARSCREEN()
	
def yewt():
    DICTATE_CAPTIONS("What do you want to watch?")
    query = str(SpeechToText())
    import webbrowser as w
    srchstring = "searching for "+ y
    DICTATE_CAPTIONS(srchstring)
    yewlink = "https://www.youtube.com/results?search_query=" + query.lower()
    w.open_new_tab(yewlink)
    CLEARSCREEN()
	
#user inputs
def alarm():
    DICTATE_CAPTIONS("Please set your alarm time: ")
    alarmHour = int(input("Hours: "))
    alarmMinute = int(input("Minutes: "))
    NOITICATION_ALARM("Alarm Setup", "time format?")
    AmPm = input("am/pm : ")

    #12 hour format
    if AmPm == "pm":
        alarmHour += 12
    #confirmation message
    msg = "Alarm set for "+ str(alarmHour) + ":" + str(alarmMinute)
	
	
# -----------------> edit from here
    NOTIFICATION_SILENT("Alarm Setup", msg)

    #setting the alarm
    while True:
        if alarmHour == datetime.datetime.now().hour:
            if alarmMinute == datetime.datetime.now().minute:
                NOTIFICATION_SILENT("Alarm","Your Alarm's ringing!")
                break
def shutdownscript():

    preak("Shutdown or restart?")
    command = str(SpeechToText())
    if command == "shutdown":
    
        DICTATE_CAPTIONS("Shutting down...")
        os.system("shutdown /s /t 1")
    elif command == "restart":
        os.system("shutdown /r /t 1")
        DICTATE_CAPTIONS("Restarting...")
    else:
        DICTATE_CAPTIONS("Invalid command")










greet_user()

while True:
    CLEARSCREEN()
    doccons = 0
    speakgate = promptless_speechToText() #listens in the background
    
    if 'harley' in speakgate.lower(): #if speech contains harley
        while True: 
            nexrem("Harley","Speak now please...")
            print("Listening...")
            x = SpeechToText()
            if "google" in x.lower():
                gewgle()
            elif "alarm" in x.lower(): 
                alarm()
            elif "play" in x.lower():
                music_play()
            elif "alarm" in x.lower():
                alarm()
            elif "power off" in x.lower():
                shutdownscript()
            elif "watch" in x.lower():
                yewt()
            elif x == "close":
                kill_app()
            elif "thank" in x.lower():
                preak("Glad to be of help")
                break #break 1st while loop
       
            #clear the console
        continue #back to line 32
    else:
        while doccons < 1:
            NOTIFICATION_SILENT("Harley",'Please call me by my name "Harley" whenever you want my help')
            doccons += 1
        continue
    

