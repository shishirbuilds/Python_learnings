# Program to import an external module and use it
# importing text to speech module : pyttsx3
# to install : python -m pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()
engine.say("i will speak this text")
engine.runAndWait()