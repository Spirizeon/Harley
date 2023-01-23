#import this to download all programme dependencies
import os
import sys
'''
note that this requires both PyAudio wheels for 64 bit and 32 bit OS (s) 
'''
def ins(pack):
    os.system("pip install "+ pack)
l = ["pywhatkit","requests","plyer","playsound","webbrowser","speech_recognition","pyttsx3","winotify"]
l2 = [".\PyAudio-0.2.11-cp310-cp310-win_amd64.whl",".\PyAudio-0.2.11-cp310-cp310-win32.whl"]
for i in l:
    ins(i)
try:
    ins(l2[0])
except: 
    print("Your python's 32 bit? No worries!")
    ins(l2[1])
os.system("cls")

print("=====================================")
print("Dependencies installed, you're good to go!")
print("=====================================")
import clearconsol