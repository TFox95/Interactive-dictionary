import json
from difflib import get_close_matches
from vTTS import recordAudio

#This is loading the json file
data = json.load(open("data.json", "r"))

def translate(w):
    """This is a function to find a word in the json file""" # <--- 
    w = w.lower()                                              
    if w in data:
        return data[w]

    matches = get_close_matches(w, data.keys()) # <--- pulled this out of all the lower parts so this is only being called once instead of 3 times. lowers complexity and runtime
    if len(matches) > 0:
        print(f'The Word you spelled was not in the dictionary. I think you meant to say this {matches[0]}?') # <--- using fstrings because they are better
        uw = str(matches[0])
        answer = input("Did you want to enter {} instead? y/n: ".format(str(matches[0]))) # <--- another superior option for string formatting but not as good as fstrings
        if answer.lower() == "y":                                                    # <--- cleaned up formatting from here....         
            return data[uw]
        elif answer.lower() == "n":
            return print("That Word Doesn't Exist!")
        else:
            return print("Input was not an option please double check it.")
    else:
        return "\nThe word you typed doesn't exist! Please double check it"          # <--- .... to here

def vtranslate():
     """This is a function to find a voice word in the json file""" # <--- 
     vwords = recordAudio()
     vwords = vwords
     for i in range(0, len(vwords)):
        if i + 5 <= len(vwords) -1 and vwords[i].lower() == "what's" and vwords[i + 1].lower() == "the" and vwords[i + 2].lower() == "definition" and vwords[i + 3].lower() == "of":
            return str(vwords[i + 4])
print(vtranslate())