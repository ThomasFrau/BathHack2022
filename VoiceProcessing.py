from test_master import *
import speech_recognition as sr
from gtts import gTTS
import os
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk
import pronouncing
import pygame
import random as rd
import time
nltk.download('punkt')
nltk.download('stopwords')

global prompt
global score
score = 0

class VP():
    def __init__(self, name):
        print("--- starting up", name, "---")
        self.name = name
        
    def speechToText(self):
        global prompt, score
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            #print(mic.list_microphone_names())
            print("listening...")
            recognizer.adjust_for_ambient_noise(mic)
            audio = recognizer.listen(mic)
        try:
            print(prompt)
            rhymes = []
            for word in prompt:
                rhymes += pronouncing.rhymes(word)
            print(rhymes)
            self.text = recognizer.recognize_google(audio)
            words = word_tokenize(self.text)
            print(words)
            stop_words = set(stopwords.words("english"))
            filtered_list = [word for word in words if word.casefold() not in stop_words]
            print(filtered_list)
            score += len(filtered_list)
            for word in words:
                if word.casefold() in prompt:
                    print(word)
                    score += 10
                if word.casefold() in rhymes:
                    print(word)
                    score += 20
    
            ##text_processing(self.text)
        except sr.UnknownValueError:
            #print("me -->  ERROR")
            score = 0
        return score
        
# Run the AI
def start_AI(prompts):
    global prompt, score
    score = 0
    prompt = prompts
    pygame.mixer.init()
    randInt = rd.randint(0, 1)
    if (randInt == 0):
        pygame.mixer.music.load("beats1.wav")
    else:
        pygame.mixer.music.load("beats2.wav")
    pygame.mixer.music.play(-1)
    time.sleep(2)
    ai = VP(name="Guys")
    text = ai.speechToText()
    pygame.mixer.music.stop()
    print(text)
    return text