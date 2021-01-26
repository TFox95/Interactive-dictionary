from os import path
import json
from decypher import decypher

data = json.load(open("data.json"))     #loads Dict. here

def history():
    """This is a function for history creatinga history file and viewing previous searched words"""
    myHistory = path.exists("searches.txt")         #Fitst we're going to check if there's a history file

    if myHistory == False:      #If there's no history file we ask the user if they would like to create a history file
        answer = input("There's no history file present on this device; would you like to create one?\n y/n: ")

        if answer == "y":
            print("History file is being created now.")
            with open("searches.txt", "w+") as myFile:     #Here we use the with command to open the file so after we finish creating and writing to the file it closes properly
                myFile.write("punch, kick")
            return "Done"

        elif answer == "n":
            return print("Skipping, No History on this device.")

    elif myHistory == True:         #If there's a history file we are going to ask if they want to view previous searched words
        answer = input("Do you want to see your previous searches? y/n: ")

        if ("y" or "yes") in answer:
            with open("searches.txt") as myFile:            # ^^ See second comment above this one
                contents = myFile.read()
                contentslist = contents.split()
            print(f"Here's your previous searches, '{contents}'")
            answer = input("Which previous word do you want to get the definition of? \nEnter here: ")
            if answer in contentslist:
                return decypher(data[answer])

        elif ("n" or "no") in answer:
            return print("Skipping previous searched words.")

    else:
        return "Error 404"

def checkHistory(value):
    myHistory = path.exists("searches.txt")
    if myHistory == True:
        answer = input(f"Do you want to save {value} in your history file?\ny/n: ")
        if answer == ("y" or "yes"):
            with open("searches.txt", "a+") as myFile:
                myFile.writelines(f"\n{value}")
                print(f"{value} has been saved in your history file!")
        if answer == ("n" or "no"):
            return print(f"{value} was not saved in history file.")
    else:
        return None
