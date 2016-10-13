from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()

    word, count = line.split('\t')

    #try:
    count = int(count)
    #except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
    #    continue

    
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print (current_word, current_count)
        current_count = count
        current_word = word
	


if current_word == word:
    print (current_word, current_count)

