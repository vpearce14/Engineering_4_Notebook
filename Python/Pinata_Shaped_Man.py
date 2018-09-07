# Pinata Shaped Man
# Written by Vincent


word = input('Hey player 1! Type in a word!')
print ("\n" *50)
n = 1
guess = ["-"]
strin = ""
wrongGuesses = 0
for x in range (1, len(word)):
   guess.append("-")
for x in guess:
        strin += x
print(strin)
while (n == 1):
    strin = ""
    wrong = True
    letter = input('Hey player 2! guess a letter!')
    for x in range (0, len(word)):
        if (letter[0] == word[x]):
            guess[x]=letter[0]
            wrong = False
    for x in guess:
        strin += x
    if (wrong == True):
        hangman = ("----","   |","   ^","  <0__/","   |==|")
        for i in range (0,wrongGuesses):
            print(hangman[i])
        wrongGuesses += 1
        if (wrongGuesses == 6):
            n = 3
        else:
            print ("That letter is not in the word")
    print(strin)
    if (strin == word):
        n = 2
    
if (n==2):
    print ("You win!!!")
if (n==3):
    print ("You lose :(")
