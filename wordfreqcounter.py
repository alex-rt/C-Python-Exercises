import re
def word_count(str):
	counter=dict()
	words=str.split()
	
	for word in words:
		if word in counter:
			counter[word]=counter[word]+1
		else:
			counter[word]=1
	return counter
			
in_text= input("type the text to check word frequency: ")
in_text= re.sub("[^a-zA-Z-\s]+", "", in_text)

print(word_count(str.lower(in_text)))