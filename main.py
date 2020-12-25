import json
from difflib import get_close_matches
from translator import translate

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