import tkinter as tk
import random as rd

from VoiceProcessing import start_AI

class gm_UI():
    def __init__(self):
        self.player1_score = 0

        self.root = tk.Tk()
        self.prompt1 = tk.StringVar()
        self.prompt1.set("Press the button for prompts")
        self.prompt = tk.Label(self.root, textvariable=self.prompt1)
        self.button = tk.Button(self.root, text= "Click me", command= self.stuff)

        self.score1 = tk.StringVar()
        self.score1.set("Score for player 1: {}".format(0))
        self.score1L = tk.Label(self.root, textvariable=self.score1)
        self.score2 = tk.StringVar()
        self.score2.set("Score for player 2: {}".format(0))
        self.score2L = tk.Label(self.root, textvariable=self.score2)
 
        self.button.pack()
        self.prompt.pack()
        self.score1L.pack()
        self.score2L.pack()
        self.root.mainloop()

    def stuff(self):

        self.player1_score += 1

        print("btn pressed")
        randInt = rd.randint(0, len(prompts) - 1)
        self.prompt1.set("Prompt is: \n{} \n{} \n{}".format(prompts[randInt][0], prompts[randInt][1], prompts[randInt][2]))
        start_AI(prompts[randInt])
        self.score1.set("Score for player 1: {}".format(self.player1_score))
        print("prompts set")

prompts = [
    ["uni", "work", "strike"],
    ["lactose", "cheese", "diarhea"],
    ["five", "guys", "burgers"],
    ["shell", "water", "turtle"],
    ["music", "guitar", "cry"],
    ["dsa", "dna", "song"],
    ["table", "chair", "spoon"]
    ]

app = gm_UI()