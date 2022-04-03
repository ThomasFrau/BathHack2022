import time
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
        self.root.configure(bg = "#1E1B1B")
        self.prompt1 = tk.StringVar()
        self.prompt1.set("Press the button for prompts")
        self.prompt = tk.Label(self.root, textvariable=self.prompt1, font=("Helvetica", 25), bg = "#1E1B1B", fg = "white")
        self.button1 = tk.Button(self.root, text= "Inspo fam", command= self.stuff1, font=("Helvetica", 25), bg = "#D3CDCB")
        self.button2 = tk.Button(self.root, text= "Spit some bars", command= self.stuff2, font=("Helvetica", 25), bg = "#D3CDCB")

        self.score1 = tk.StringVar()
        self.score1.set("Score for player 1: {}".format(0))
        self.score1L = tk.Label(self.root, textvariable=self.score1, font=("Helvetica", 25), bg = "#1E1B1B", fg = "white")
        self.score2 = tk.StringVar()
        self.score2.set("Score for player 2: {}".format(0))
        self.score2L = tk.Label(self.root, textvariable=self.score2, font=("Helvetica", 25), bg = "#1E1B1B", fg = "white")
 
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
        if self.flag:
            self.clearJSON()
            self.prompt1.set("Player 1 \n Prompt is: \n{} \n{} \n{}".format(prompts[randInt][0], prompts[randInt][1], prompts[randInt][2]))
        else:
            self.prompt1.set("Player 2 \n Prompt is: \n{} \n{} \n{}".format(prompts[randInt][0], prompts[randInt][1], prompts[randInt][2]))

    def stuff2(self):
        if(self.flag):
            self.player1_score += 0.6 * start_AI(prompts[randInt])
            # self.score1.set("Score for player 1: {}".format(self.player1_score))
        else:
            self.player2_score += 0.6 * start_AI(prompts[randInt])
            self.root.after(15000)
            score_tuple = self.readJSON()
            self.player1_score += 0.4 * score_tuple[0]
            self.player2_score += 0.4 * score_tuple[1]
            self.score2.set("Score for player 2: {}".format(int(self.player2_score)))
            self.score1.set("Score for player 1: {}".format(int(self.player1_score)))
            if (self.player1_score > self.player2_score):
                self.prompt1.set("And the winner is! {}".format("Player 1"))
            else:
                self.prompt1.set("And the winner is! {}".format("Player 2"))


prompts = [
    ["uni", "work", "strike"],
    ["awesome", "paradise", "cry"],
    ["street", "gangster", "block"],
    ["coding", "debug", "git"],
    ["duck", "lake", "library"],
    ["cowboy", "west", "horse"],
    ["church", "god", "religion"],
    ["hack", "sleep", "timer"],
    ["London", "ends", "shank"],
    ["live", "love", "laugh"],
    ["hot", "sun", "mum"],
    ["duolingo", "toes", "home"]
    ]

app = gm_UI()