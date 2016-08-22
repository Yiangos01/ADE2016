import sys

mape=open("mapperout.txt",'w')
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        mape.write(word+"\t1\n")
mape.close()
