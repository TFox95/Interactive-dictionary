import json
from difflib import get_close_matches

#This is loading the json file
data = json.load(open("data.json", "r"))

def translate(w):
    """This is a function to find a word in the json file""" # <--- use docstrings
    w = w.lower()                                              # <--- also cleaned up this little block before matches
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


def main(): # <--- created a main class for the items that were just floating, this is better etiquette
    word = input("Enter a Word: ") # <--- changed the value from w to word, try to have variables be as descriptive as possible, but at the same time simple
    output = translate(word)
    if type(output) == list:                        # <--from here
        for i in output:
            print("\n%s" % i, sep="\n")
    elif type(output) == str:
        print(output)
    else:
        print("Error 404")                          # <--to here all I did was change the formatting


if __name__ == "__main__": # <--- this is generally used to kick off running the program
    main()