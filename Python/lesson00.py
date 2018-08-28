# Automatic Dice Roller
# Written by Vincent

from random import randint
#import keyboard

print ("Automatic Dice Roller")

#print ("Press enter to roll or x then enter to exit")

while True:
   text = input('Press enter to roll or x then enter to exit')
   if text == '':
       print (randint(1,6))
   if text == 'x':
       break
