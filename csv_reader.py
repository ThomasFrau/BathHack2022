import random as r

prompts = [
    ["uni", "work", "strike"],
    ["lactose", "cheese", "diarhea"],
    ["five", "guys", "burgers"],
    ["shell", "water", "turtle"],
    ["music", "guitar", "cry"],
    ["dsa", "dna", "song"],
    ["table", "chair", "spoon"]
    ]

r.seed(42)
for i in range(10):
    print(prompts[r.randint(0, len(prompts))])