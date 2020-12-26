import json

class loadfile():
	def __init__(self, dict=None):
		if data is None:
			data = {}
		else:
			with open("data.json", "r") as wordFile:
				self.content = wordFile.read()