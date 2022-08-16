import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime




listener = sr .Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
        engine.say(text)
        engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa')
                print(command)
    except:
        pass
    return command

def run_alexa():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('playing','')
            talk('playing' +song)
            pywhatkit.playonyt(song)
        elif 'play ' in command:
            status = command.replace('playing','')
            talk('playing' +status)
            pywhatkit.playonyt(song)
        elif 'play' in command:
            movies = command.replace('playing')
            talk('playing' +movies)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(time)
            print(time)
        elif 'crazy' in command:
            talk('i am not crazy and your a crazy')
            print(talk)
        elif 'time' in command:
            current_time = datetime.datetime.now()
            talk('current time is:',current_time)
            print('current time is:',current_time)

        else:
            talk('please say the command again')


while True:
    run_alexa()
   