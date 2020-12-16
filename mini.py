
#importing the required libraries
import speech_recognition as sp
import pyttsx3
import pywhatkit as pwk
import wikipedia as wk
import datetime as dt
import weather_forecast as wf
from GoogleNews import GoogleNews
import random
import pyjokes




#import packages for automation
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


#Ssetting a variable name for speech recognition and text to speech
hear=sp.Recognizer()
engine = pyttsx3.init()

#changing the assistant voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#changing voice speed
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate',125)

#creating a function for text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

def loop():
    try:
        #Recognising the voice
        with sp.Microphone() as source:
            print('Hey... Adio here ')
            speak('Hey..adio here? how can i help u')
            voice=hear.listen(source)
            command = hear.recognize_google(voice)
            command = command.lower()
            print(command,'...')
            
        #Playing songs/videos on youtube
            if 'play' in command:
                command=command.replace('play','')
                print('playing'+command)
                pwk.playonyt(command)
            
            
        #wikipedia
            elif 'who' in command:
                command=command.replace('who is','')
                wiki=wk.summary(command,sentences=1)
                print(wiki)
                speak(wiki)
        
        
        #date and time using datetime library
            elif 'date' in command:
                date=dt.datetime.now().strftime('%d %B %Y %A')
                print(date)
                speak(date)
            
            elif 'time' in command:
                time=dt.datetime.now().strftime('%H %M %p')
                print(time)
                speak(time)
            #automate to shop on amazon   
            elif 'amazon' in command:
                command=command.replace('on amazon','')
                url='https://www.amazon.in/'
                driver=webdriver.Chrome(ChromeDriverManager().install())
                driver.get(url)
                driver.set_page_load_timeout(10)
                driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys(command);
                search=driver.find_element_by_xpath('//*[@id="nav-search-submit-text"]/input')
                search.click()
                
            elif 'flipkart' in command:
                command=command.replace('on flipkart','')
                url='https://www.flipkart.com/'
                driver=webdriver.Chrome(ChromeDriverManager().install())
                driver.get(url)
                driver.set_page_load_timeout(10)
                driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').send_keys(command);
                driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()
                search=driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button/svg')
                search.click()
                
                
        #google search
            elif 'search' in command:
                command=command.replace('search','')
                pwk.search(command)
            
        #jokes using pyjokes library   
            elif 'joke' in command:
                joke=pyjokes.get_jokes(language="en",)
                
                speak(joke[(random.randint(1, 5))])
                
                
                
        #Weather updates using Weather_forecast library
            elif 'weather' in command:
                
                if 'in' in command:
                    com=command.split('in',1)
                    loc=com[1].capitalize()
                    speak(wf.forecast(loc),time=dt.datetime.now().strftime('%X'),date=dt.datetime.now().strftime('%x'))
                else:
                    speak('Please repeat the question with location')
            
        #News updates using GoogleNews library     
            elif 'news' in command:
                ggn = GoogleNews('en')
                
                if 'about' in command:
                    com=command.split('about',1)
                    newz=com[1].capitalize()
                    ggn.search(newz)
                    ggn.getpage(1)
                    print(ggn.gettext())
                    speak(ggn.gettext())
                if 'on' in command:
                    com=command.split('on',1)
                    newz=com[1].capitalize()
                    ggn.search(newz)
                    ggn.getpage(1)
                    print(ggn.gettext())
                    speak(ggn.gettext())  
                
                else:
                    ggn.search('India')
                    ggn.getpage(0)
                    print(ggn.gettext())
                    speak(ggn.gettext())
                    
                        
                
                
            else:
                pwk.search(command)
                
                
                
    except:
        pass



while True:
    loop()
    




    



