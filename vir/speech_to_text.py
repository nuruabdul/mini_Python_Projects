#Install speech recognition and audio using the commands below.
#pip install SpeechRecognition & pip install PyAudio.


# from requests_html import HTMLSession
# import speak
import speech_recognition as sr 
from requests_html import HTMLSession
import speak


def speech_to_text():
    r =  sr.Recognizer()
    with sr.Microphone() as source:
      audio = r.listen(source) # methord 
      voice_data = ''
      try:
        voice_data = r.recognize_google(audio)
        return voice_data

      except sr.UnknownValueError:
             speak.speak("sorry")
      except sr.RequestError:
            speak.speak('No internet connect please turn on you internet')  


