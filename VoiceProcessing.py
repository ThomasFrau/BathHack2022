from test_master import *
import speech_recognition as sr
from gtts import gTTS
import os
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk
import pronouncing
nltk.download('punkt')
nltk.download('stopwords')

global prompt

class VP():
    def __init__(self, name):
        print("--- starting up", name, "---")
        self.name = name
        
    @staticmethod
    def text_processing(text):
        print("tokenising!!")
        
    def speechToText(self):
        global prompt
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
            for word in filtered_list:
                if word in prompt:
                    print(word)
                if word in rhymes:
                    print(word)
    
            ##text_processing(self.text)
        except sr.UnknownValueError:
            print("me -->  ERROR")
            
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
    global prompt
    prompt = prompts
    ai = VP(name="Guys")
    while True:
        ai.speechToText()
     ## wake up
        if ai.wake_up(ai.name) is True:
            res = "Hello I am Maya the AI, what can I do for you"
            print(res)
            text_to_speech(res)