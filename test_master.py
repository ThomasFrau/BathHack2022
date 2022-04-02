class Test_master():
    def __init__(self):
        print("Game master created")

    def prompts():
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
        return (prompts[r.randint(0, len(prompts))])