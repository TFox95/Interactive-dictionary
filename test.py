a = ['a', 'b', 'c']
str =  "a123"

a_match = [True for match in a if match in str]

if True in a_match:
	print("some of the strings found in str")
else:
	print("no strings found in str")