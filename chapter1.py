#                    "CHAPTER 01 - MODULES,COMMAND & PIP"
#  Module to covert text into voice
import pyttsx3
engine = pyttsx3.init() # object creation                    
engine.setProperty('rate', 125)                        
engine.setProperty('volume',100.0)  
"""VOICE"""
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[0].id)   


engine= pyttsx3.init()
engine.say("hey everyone kya haal hai ")
engine.runAndWait()

# import os
# directory_path = '/hp'
# contents = os.listdir(directory_path)
# for item in contents: 
#     print(item)