import tkinter as tk
import random as rd
import json

from VoiceProcessing import start_AI

global randInt
class gm_UI():
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self.flag = False
        self.root = tk.Tk()
        self.prompt1 = tk.StringVar()
        self.prompt1.set("Press the button for prompts")
        self.prompt = tk.Label(self.root, textvariable=self.prompt1, font=("Helvetica", 25))
        self.button1 = tk.Button(self.root, text= "Click me for prompts", command= self.stuff1, font=("Helvetica", 25))
        self.button2 = tk.Button(self.root, text= "Click me to start AI", command= self.stuff2, font=("Helvetica", 25))

        self.score1 = tk.StringVar()
        self.score1.set("Score for player 1: {}".format(0))
        self.score1L = tk.Label(self.root, textvariable=self.score1, font=("Helvetica", 25))
        self.score2 = tk.StringVar()
        self.score2.set("Score for player 2: {}".format(0))
        self.score2L = tk.Label(self.root, textvariable=self.score2, font=("Helvetica", 25))
 
        self.button1.pack()
        self.button2.pack()
        self.prompt.pack()
        self.score1L.pack()
        self.score2L.pack()
        self.root.geometry("500x450+10+10")
        self.root.mainloop()

    def readJSON(self):
        file = open("polling/server/data.json", "r")
        jsonObject = json.load(file)
        file.close()
        return jsonObject["Rapper1"], jsonObject["Rapper2"]

    def clearJSON(self):
        file = open("polling/server/data.json", "w")
        data = {
            "Rapper1":0,
            "Rapper2":0
        }
        json.dump(data, file)
        file.close()

    def stuff1(self):
        global randInt
        self.flag = not self.flag
        print("btn pressed")
        randInt = rd.randint(0, len(prompts) - 1)
        print(self.clearJSON())
        if self.flag:
            self.prompt1.set("Player 1 \n Prompt is: \n{} \n{} \n{}".format(prompts[randInt][0], prompts[randInt][1], prompts[randInt][2]))
        else:
            self.prompt1.set("Player 2 \n Prompt is: \n{} \n{} \n{}".format(prompts[randInt][0], prompts[randInt][1], prompts[randInt][2]))

    def stuff2(self):
        if(self.flag):
            self.player1_score += start_AI(prompts[randInt])
            self.score1.set("Score for player 1: {}".format(self.player1_score))
        else:
            self.player2_score += start_AI(prompts[randInt])
            self.score2.set("Score for player 2: {}".format(self.player2_score))

prompts = [
    ["uni", "work", "strike"],
    ["lactose", "cheese", "diarrhoea"],
    ["five", "guys", "burgers"],
    ["shell", "water", "turtle"],
    ["music", "guitar", "cry"],
    ["dsa", "dna", "song"],
    ["table", "chair", "spoon"]
    ]

app = gm_UI()