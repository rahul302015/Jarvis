import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import googlesearch
import webbrowser
import os
import smtplib
import random
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#To greet the user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Fryday Sir. Please tell me how may I help you")       
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('lastyearproject47@gmail.com', 'lastyearproject')
    server.sendmail('lastyearproject47@gmail.com', to, content)
    server.close()
    

if _name_ == "_main_":
    #speak("My name is Fryday")
    wishMe()
    speak("Enter Passcode")
    listOfCommands=[]
    passCode=takeCommand().lower()
    if "blue" in passCode:
        speak('Correct passCode')
        speak('What can I do for you sirrr')
        while True:
        # if 1:
            query = takeCommand().lower()
            listOfCommands.append(query)

            # Logic for executing tasks based on query
            #for wikipedia search
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            
            elif 'search google' in query:
                speak('What do You wanna search')
                content = takeCommand()
                speak('Searching Google.... errrrr')
                content =  content.replace("google" , " ")
                speak(f"opening {content}.com")
                webbrowser.open(f"{content}.com")

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")
                speak("Opening Google")
         
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
            
            elif 'maps' in query:
                speak('Where do you wanna go')
                content = takeCommand()
                speak('Searching Google maos')
                content =  content.replace("google" , " ")
                speak(f"opening route to {content}")
                webbrowser.open(f"https://www.google.com/maps/place/{content}")


            elif 'open songs' in query:
                notePath = "D:\\Raghav\\Raghav\\Songs"
                os.startfile(notePath)
            
            elif 'close friday' in query:
                speak("Do you want to see list of executed Commands")
                commands=takeCommand().lower()
                if 'yes' in commands:
                    print(listOfCommands)
                    speak(listOfCommands)
                    speak('Thanks For Using me Sir, Have a great day ahead')
                else:
                    speak('Thanks For Using me Sir, Have a great day ahead')
                    break
                break

            elif "temperature" in query:
                speak("Please say the name of Place whose temprature you want to know")
                temp=takeCommand().lower()
                speak("Searching Temprature on Google")
                temp =  temp.replace("google" , " ")
                speak(f"Showing temprature of {temp}")
                webbrowser.open(f"Temprature of {temp}")
            
            elif "password" in query:
                x=random.randint(1000,9999)
                s=smtplib.SMTP("smtp.gmail.com",587)
                s.starttls()
                s.login('lastyearproject47@gmail.com', 'lastyearproject')
                speak("Enter your personal mail id")
                mailid=input("Enter Mail id :  ")
                s.sendmail('lastyearproject47@gmail.com',mailid,"this is otp to execute Fryday Commands {}".format(x))
                speak("To Access This feature , Please Enter Passcode")
                print(" Enter the recived fryday otp ")
                otp=int(input())
                if otp == x :
                    notePath = "D:\\Raghav\\Raghav\\backup"
                    os.startfile(notePath)
                else:
                    speak("wrong one time password")
            
            elif 'track' in query:
                speak("Enter Phone Number")
                tracker=input("Enter Number with country code and plus sign : ")
                ch_num = phonenumbers.parse(tracker,"CH")
                ser_num = phonenumbers.parse(tracker,"RO")
                countryName=(geocoder.description_for_number(ch_num,"en"))
                serviceProviderName=(carrier.name_for_number(ser_num,"en"))
                print(countryName,serviceProviderName)
                speak(countryName)
                speak(serviceProviderName)

            elif 'send email' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    speak("Enter Email id")
                    #to = takeCommand()
                    to = input("Enter Email id : ")
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry Sir. I am not able to send this email")    
            
    else:
        speak("Wrong PassCode")