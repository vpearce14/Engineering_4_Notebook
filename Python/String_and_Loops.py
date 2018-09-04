# Strings and Loops
# Written by Vincent

sentence = input('write a sentence')
sentence = sentence.split( )
for x in range(0, len(sentence)):
    print ("-")
    for t in range(0, len(sentence[x])):
        print (sentence[x][t])
