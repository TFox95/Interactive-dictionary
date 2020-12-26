import speech_recognition as sr
from gtts import gTTS

def recordAudio():
	""" This is a function to Record audio"""
	vdata = str("")
	r = sr.Recognizer() # Creating a recognizer object
	with sr.Microphone() as source:
		print("say Word: ")  #for testing purposes only; if it works comment this whole line
		audio = r.listen(source)

		try: # use Google's Speech Recognition
			vdata = r.recognize_google(audio)
			print(f"you said, \"{vdata}\"")
		except sr.UnknownValueError: # This will allow us to check for unknown errors
			print("Google Speech Recognition could not understand error, unknown error")
			return vdata
		except sr.RequestError as re:
			print("Request results from Google Speech Recognition service error" + re) # This is incase if I get disconnected 

		return vdata