# Pinata Shaped Man
# Written by Vincent


word = input('Hey player 1! Type in a word!')
print ("\n" *50)
n = False
while (n == False):
    hangman = ("----","   |","   ^","  <0__/","   |==|")
    for i in hangman:
        print (i)
    for x in range (0, len(word)):
        print ("_ ", end = "")
    letter = input('Hey player 2! guess a letter!')
    for x in range (0, len(word)):
        if (letter[0] == word[x]):
            print(letter, end = " ")
        else:
            print ("_ ", end = "")
