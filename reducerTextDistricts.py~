from operator import itemgetter
import sys

current_word = None
word = None
paragraph = None
current_paragraph = None 
first=1

for line in sys.stdin:
    line = line.strip()
	
    word, text = line.split('\t')
    if(word!=None):
    	if current_word == word:
        	print(text+"\n")
    	else:
        	if current_word:
			print(word)		
			print(text+"\n")
        	current_paragraph = text+"\n"
        	current_word = word
	
if current_word == word:
    print(current_word)
    print(text)

