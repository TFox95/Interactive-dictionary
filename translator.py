import json
from difflib import get_close_matches
from vTTS import recordAudio
from decypher import decypher
from history import checkHistory

#This is loading the json file
data = json.load(open("data.json", "r"))

def translate():
    """This is a function to find a word in the json file"""
    w = input("What word do you want to search?\nEnter here: ")
    w = w.lower()

    if w in data:
        checkHistory(w)
        output = data[w]
        return decypher(output)

    matches = get_close_matches(w, data.keys()) # <--- pulled this out of all the lower parts so this is only being called once instead of 3 times. lowers complexity and runtime
    if len(matches) > 0:
        print(f'The Word you spelled was not in the dictionary. I think you meant to say this, \"{matches[0]}\"?') # <--- using fstrings because they are better
        uw = str(matches[0])
        answer = input("Did you want to enter {} instead? y/n: ".format(str(matches[0]))) # <--- another superior option for string formatting but not as good as fstrings

        if answer.lower() == "y":                                                    # <--- cleaned up formatting from here....
            checkHistory(uw)
            output = data[uw]
            return decypher(output)

        elif answer.lower() == "n":
            return print("That Word Doesn't Exist!")
        else:
            return print("Input was not an option please double check it.")
    else:
        return print("\nThe word you typed doesn't exist! Please double check it")          # <--- This is just encase the word doesn't exist

def vtranslate():
     """This is a function to find a voice word in the json file""" # <---
     vQuestion = False
     while vQuestion == False:
        vword = recordAudio()
        vword = vword.lower()
        if str("what's the definition of ") in vword:
            vQuestion = True
            vlist = vword.split()
            if vlist[-1] in data:
                checkHistory(vlist[-1])
                output = data[vlist[-1]]
                return decypher(output)