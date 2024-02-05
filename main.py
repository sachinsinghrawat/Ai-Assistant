import speech_recognition as sr
import win32com.client
import webbrowser
import os
import datetime
from datetime import  date
import  AppOpener
from AppOpener import  open , close
from openai import OpenAI


def other(prompt):
    client = OpenAI(api_key="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")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},

        ],
        temperature=0.7,
        max_tokens=70,
        
    )

    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    try:
        print("Jarvis said :- "+ completion.choices[0].message.content)
        speaker.Speak(completion.choices[0].message.content)
    except Exception as e:
        print(e)




def listen():
    print("listening ... ")
    r = sr.Recognizer()
    my_mic = sr.Microphone()

    with my_mic as source:
        print("say now")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio , language="en-in")

        except Exception as e:
            query = "sorry";

        return query;



def navigate(say):
    if "open google" in say.lower():
        webbrowser.open("https://www.google.com")
        speaker.Speak("Sir , open google")

    elif "open youtube" in say.lower():
        webbrowser.open("https://www.youtube.com")
        speaker.Speak("hope you will enjoyed it ")

    elif "open instagram" in say.lower():
        webbrowser.open("https://www.instagram.com")
        speaker.Speak("Sir , have fun")

    elif "open chrome" in say.lower():
        webbrowser.open("https://www.chrome.com")
        speaker.Speak("Sir , call me again ")


    elif "wikipedia" in say:
        webbrowser.open("https://www.wikipedia.com")
        speaker.Speak("Ok sir ")


    elif "time" in say.lower():
        time = datetime.datetime.now().strftime("%H:%M:%S");
        dat = datetime.date
        speaker.Speak(f"Sir the time is {time}")

    elif "date" in say.lower():
        time = datetime.datetime.now().date();
        speaker.Speak(f"Sir the date is {time} ")

    elif "camera" in say.lower():
        open("camera")
        speaker.Speak("Camera open sir !")

    elif "map" in say.lower():
        if "open map" in say.lower():
            speaker.Speak("here is your map sir ")
            open("maps")

        elif "close the map" in say.lower():
            speaker.Speak("Closing Map Sir")
            close("maps")


    elif "media" in say.lower():
        if "open media player" in say.lower():
            open("Media Player")

        elif "close media player" in say.lower():
            close("Media Player")


    elif "spotify" in say.lower():
        if "open spotify" in say.lower():
            speaker.Speak("i am opening spotify")
            open("Spotify")

        elif "close spotify" in say.lower():
            speaker.Speak("i am closing spotify ")
            close("Spotify")


    elif "calculator" in say.lower():
        if "open calculator" in say.lower():
            speaker.Speak("opening calculator sachin")
            open("calculator")

        elif "close the calculator" in say.lower():
            close("calculator")

    elif "visual studio" in say.lower():
        if "open visual studio" in say.lower():
            open("Visual Studio Code")

        elif "close the visual studio" in say.lower():
            close("Visual Studio Code")

    elif "who is your creator" in say.lower():
        speaker.Speak("My creator is Sachin ")

    elif "stop" in say.lower():
        speaker.Speak("call Me again Sir .. ")
        exit()


    else:
        other(say)





speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    say = listen()
    print("user said :-  " + say  )
    navigate(say)







