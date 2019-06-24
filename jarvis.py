import speech_recognition as sr 
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from elasticsearch import Elasticsearch 
import random

r=sr.Recognizer()

mic=sr.Microphone()
# print("Listening")

def say(text):
    subprocess.call(['say',text])

def searchGoogle(query):
    browser=webdriver.Chrome()
    browser.get('http://www.google.com')
    search=browser.find_element_by_name('q')
    search.send_keys(query)
    search.send_keys(Keys.RETURN)

# searchGoogle('Open Google')

# with mic as source:
#     r.adjust_for_ambient_noise(source)
#     audio=r.listen(source)
#     transcript=r.recognize_google(audio)
#     print(transcript)
#     searchGoogle(transcript)

def activate(phrase='Hello'):
    with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            transcript = r.recognize_google(audio)
            if transcript.lower() == phrase:
                return True
            else:
                return False

    
        
doneText=['I got these results for you','Found it!!','Wohoooo I got it']
toSay=random.choice(doneText)
# print(randomDoneText)
    
while True:
    if activate() == True:
        try:
            say("Hey Anirudh, how can I help you today?")
            with mic as source:
                print('Say Something!')
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                transcript = r.recognize_google(audio)
                searchGoogle(transcript)
                say(toSay)
                
                    
                   
                
        except:
            pass
    else:
        pass






