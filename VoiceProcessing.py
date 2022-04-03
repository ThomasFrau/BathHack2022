from test_master import *
import speech_recognition as sr
from gtts import gTTS
import os
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk
import pronouncing
import pygame
nltk.download('punkt')
nltk.download('stopwords')

global prompt
global score
score = 0

class VP():
    def __init__(self, name):
        print("--- starting up", name, "---")
        self.name = name
        
    @staticmethod
    def text_processing(text):
        print("tokenising!!")
        
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
            #print(rhymes)
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
            print("me -->  ERROR")
        return score
            
    def wake_up(self, text):
        return True if self.name in text.lower() else False

    @staticmethod
    def text_to_speech(text):
        print("ai --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        os.system("start res.mp3")  #macbook->afplay | windows->start
        os.remove("res.mp3")
        


# Run the AI
def start_AI(prompts):
    global prompt, score
    score = 0
    prompt = prompts
    pygame.mixer.init()
    pygame.mixer.music.load("beats1.wav")
    pygame.mixer.music.play(-1)
    ai = VP(name="Guys")
    text = ai.speechToText()
    pygame.mixer.music.stop()
    print(text)
    return text