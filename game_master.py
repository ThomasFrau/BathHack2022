import json


prompts = [
    ["uni", "work", "strike"],
    ["lactose", "cheese", "diarhea"],
    ["five", "guys", "burgers"],
    ["shell", "water", "turtle"],
    ["music", "guitar", "cry"],
    ["dsa", "dna", "song"],
    ["table", "chair", "spoon"]
    ]

dictionary = {
    "prompt" : prompts[0],
    "score" : 100
}

json_object = json.dumps(dictionary, indent = 4)
file = open ("sample.json", "wt") 
file.write(json_object)