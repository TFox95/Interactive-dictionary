from os import path

myHistory = path.exists("searches.txt")

if myHistory == True:
	print("Skipping, No history on this device")
elif myHistory == False:
	answer = input("Do you want to see your previous searches? y/n: ")
	if answer == "y":
		with open("searches.txt", "w+") as myFile:
			myFile.write("kick\npunch\nslap\nthrow\nslam\n")
			contents = myFile.read()
			print(contents)

		print(f"here's your previous searches: {contents}")