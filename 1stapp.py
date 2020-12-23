#First import json

import json
from difflib import get_close_matches


#This is loading the json file
data = json.load(open("data.json", "r"))



#This is a function to find a word in the json file
def translate(w):
	#making sure w is always constantly a lower input
	w = w.lower()
	#If the word is in the file return the value
	if w in data:
		 for i in data[w]:
		 	return "\n%s" % i 


	#if a Word is not in the file return spellcheck warning	
	elif len(get_close_matches(w, data.keys())) > 0:

	 print("The Word you spelled was not in the dictionary. I think you meant to say this %s?" % (get_close_matches(w, data.keys())[0])) 

	 uw = str((get_close_matches(w, data.keys())[0]))
 	
 	#Now we are asking for a y for yes or a n for no to still execute the program
	 answer = input("Did you want to enter %s instead? y/n: " % str(get_close_matches(w, data.keys())[0]))

	 if answer.lower() == "y":

	 		#now we need to take the crrected word and make it the variable 		 
	 	for i in data[uw]:
	 		return "\n%s" % i

	 elif answer.lower() == "n":

	 	return "That Word Doesn't Exist!"

	 else:

	 	return "Input was not an option please double check it."

	 #Else if there is no possible word return a no such word phrase
	else:
		return "\nThe word you typed doesn't exist! Please double check it"

w = input("Enter a Word: ")


print(translate(w))