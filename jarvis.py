import datetime
import os
import smtplib
import sys
import time
import webbrowser
import winsound
from threading import *
from tkinter import *
import wolframalpha
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import requests
import subprocess

print("Initializing Alexa....")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty("rate", 140)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Your Assistant, Please tell me how may I help you")       

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
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":


    wishMe()
    while True:
    # if 1:


        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:


            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'tell me about yourself' in query:
            speak("I am a voice-controlled virtual personal assistant thats changing the way we interact with technology.")

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'wish Me' in query:
            speak("Good Afternoon Sir!")


        elif 'live match' in query:
            webbrowser.open("https://www.hotstar.com/in/sports/cricket/icc-mens-t20-world-cup-2022/m706920/live-streaming/1540019065")
            speak("Opening Live Match")
            

        elif 'live score' in query:
            webbrowser.open("https://www.cricbuzz.com/cricket-match/live-scores")
            speak("Opening Live Score")
            time.sleep(15)


        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Google")


        elif 'open netflix' in query:
            webbrowser.open("https://www.netflix.com/in/")
            speak("Opening Netflix")


        elif "weather report" or "temperature" in query:

            api_key="adca572add04dcfd62ce4f954e354b08"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()



            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))


        elif 'news' in query:

            webbrowser.open("https://timesofindia.indiatimes.com/?from=mdr")
            speak('Here are some headlines from the Times of India, Happy reading')
            time.sleep(60)



        elif 'who are you' in query or 'what can you do' in query:

            speak('I am Alexa, your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')



        elif "who made you" in query or "who created you" in query or "who build you" in query:

            print("I was build by Vishwas ")
            speak("I was build by Vishwas")



        elif 'ask' in query:

            print('I can answer to computational and geographical questions and what question do you want to ask now?')
            speak('I can answer to computational and geographical questions and what question do you want to ask now?')
            question=takeCommand()
            app_id="7W2R36-GHE5T7XKLH"
            client = wolframalpha.Client('7W2R36-GHE5T7XKLH')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)



        elif 'open stackoverflow' in query:

            print("Opening Stackoverflow...")
            speak("Opening Stackoverflow...")
            webbrowser.open("stackoverflow.com") 
            

        elif 'play music' in query:

            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'search' in query:
            
            try:
   
                    # it will perform the Google search
                        find = query.replace('search', '')
                        speak('Searching ' + find)
                        pywhatkit.search(find)
                        print("Searching...")
                        time.sleep(15)
 
            except:
   
                    # Printing Error Message
                        print("An unknown error occurred")
        

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")


        elif 'open code' in query:
            codePath = "Your Code Path"
            os.startfile(codePath)


        elif 'email to Vishwas' in query:

            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vishwasgupta666@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")    

        elif 'close' in query:
            
            print("Bye Sir! Have a Good Day.")
            speak("Bye Sir! Have a good day.")
            sys.exit()


        elif "shutdown" in query or "off computer" in query:
            print("Ok , Your pc will shutdown in 10 sec make sure you exit from all applications.")
            speak("Ok , Your pc will shutdown in 10 sec make sure you exit from all applications.")
            subprocess.call(["shutdown", "/l"])
			
            time.sleep(10)
            
        elif 'set alarm' in query:
            
            # Create Object
            root = Tk()
            
            # Set geometry
            root.geometry("400x200")
            
            # Use Threading
            def Threading():
                t1=Thread(target=alarm)
                t1.start()
            
            def alarm():
                # Infinite Loop
                while True:
                    # Set Alarm
                    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
            
                    # Wait for one seconds
                    time.sleep(1)
            
                    # Get current time
                    current_time = datetime.datetime.now().strftime("%H:%M:%S")
                    print(current_time,set_alarm_time)
            
                    # Check whether set alarm is equal to current time or not
                    if current_time == set_alarm_time:
                        print("Time to Wake up")
                        # Playing sound
                        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            
            # Add Labels, Frame, Button, Optionmenus
            Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
            Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()
            
            frame = Frame(root)
            frame.pack()
            
            hour = StringVar(root)
            hours = ('00', '01', '02', '03', '04', '05', '06', '07',
                     '08', '09', '10', '11', '12', '13', '14', '15',
                     '16', '17', '18', '19', '20', '21', '22', '23', '24'
                    )
            hour.set(hours[0])
            
            hrs = OptionMenu(frame, hour, *hours)
            hrs.pack(side=LEFT)
            
            minute = StringVar(root)
            minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
                       '08', '09', '10', '11', '12', '13', '14', '15',
                       '16', '17', '18', '19', '20', '21', '22', '23',
                       '24', '25', '26', '27', '28', '29', '30', '31',
                       '32', '33', '34', '35', '36', '37', '38', '39',
                       '40', '41', '42', '43', '44', '45', '46', '47',
                       '48', '49', '50', '51', '52', '53', '54', '55',
                       '56', '57', '58', '59', '60')
            minute.set(minutes[0])
            
            mins = OptionMenu(frame, minute, *minutes)
            mins.pack(side=LEFT)
            
            second = StringVar(root)
            seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
                       '08', '09', '10', '11', '12', '13', '14', '15',
                       '16', '17', '18', '19', '20', '21', '22', '23',
                       '24', '25', '26', '27', '28', '29', '30', '31',
                       '32', '33', '34', '35', '36', '37', '38', '39',
                       '40', '41', '42', '43', '44', '45', '46', '47',
                       '48', '49', '50', '51', '52', '53', '54', '55',
                       '56', '57', '58', '59', '60')
            second.set(seconds[0])
            
            secs = OptionMenu(frame, second, *seconds)
            secs.pack(side=LEFT)
            
            Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)
            
            # Execute Tkinter
            root.mainloop()
