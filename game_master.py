import tkinter as tk
import random as rd

prompts = [
    ["uni", "work", "strike"],
    ["lactose", "cheese", "diarhea"],
    ["five", "guys", "burgers"],
    ["shell", "water", "turtle"],
    ["music", "guitar", "cry"],
    ["dsa", "dna", "song"],
    ["table", "chair", "spoon"]
    ]

window = tk.Tk()
currPrompt = prompts[rd.randint(0, len(prompts))]
label = tk.Label (text="The prompt is: \n {} \n {} \n {}".format(currPrompt[0], currPrompt[1], currPrompt[2]) )
label.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()

window.mainloop()
