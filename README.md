# Hey, next years folks!!

Here's some helpful tips:
1. Join BACON! you'll learn engineering skills twice as fast and make cool nerd friends
2. Choose your partners wisely. It's much more important to have someone who motivates you than someone you can socialize with
3. Focus on one thing at a time.
4. To stack stls, open them in meshmixer, add a very thin cylinder, make it very small, then merge all parts.
5. And most importantly: Everything has a price. 3D printing, servos, arduinos, and motors are all expensive. Don't waste anything!!

# Engineering 4 Notebook

This is where all my stuff will go!

## Hello Python

### Lessons Learned

My first ever real python script! All I had to do was print "hello world!" This lesson showed me how much formatting mattered in Python. A single space messed up my code and took me half a class period to find. Also, It's important to know what version of Python you're using. in other versions, a keyboard input prompt gets called "raw.input()" whereas in the version I had was called "input()".

### Code

https://github.com/vpearce14/Engineering_4_Notebook/blob/master/Python/Hello_Python.py

## Python Calculator

### Lessons Learned

In this assignment, the program prompted for two values, then ran them through a series of equations, printing the result. Combining strings and variables happens with commas, not plus symbols. Functions are declared with "def". Inputs will be strings unless converted into something else. I discovered that when an error only occured at the subrtracting equation.

### Code

https://github.com/vpearce14/Engineering_4_Notebook/blob/master/Python/Calculator.py

## Python Quadratic Solver

### Lessons Learned

In this assignment, I made a python sript that would prompt for three numbers then put them into the quadratic equation. I learned that when you edit a file, you have to re-add it to git or it won't commit. It's also important to remember to add parenthesis when doing convoluted math problems.

### Code

https://github.com/vpearce14/Engineering_4_Notebook/blob/master/Python/Quadratic_Solver.py

## Strings and Loops

### Lessons Learned

In this assignment, my program would prompt for a string, then print it out one letter at a time. The key to figuring out this assignment is that when the sentence is split, the assigned variable becomes a list. In the list, each word has a set place that can be found using [numbers]. Then, each word within that list is a string, the characters in which can also be found with [numbers]. A cool thing I found is that these [numbers] can be stacked[][].

### Code

https://github.com/vpearce14/Engineering_4_Notebook/blob/master/Python/Loops_and_Strings.py

## Pinata Shaped Man

### Lessons Learned

In this one I had to make a hangman game. Dr. Shields' advice is sound: take small bites. This assignment was pretty complex so it helped to just go layer by layer and do lots of small tests. Another thing that was helpful was to use an array to store the user's current guesses, then attach the characters in the array into a string before printing them.

### Code 

https://github.com/vpearce14/https://github.com/vpearce14/Engineering_4_Notebook/blob/master/Python/Pinata_Shaped_Man.py

## GPIO Bash

### Lessons Learned

This was our intro to gpio, where we would turn on and LED using a pi bash script. The first step of this assignment was to solder male-male headers onto the pi. This gave me the most amount of trouble, as I had plugged the header into a breadboard to secure it. When I tried to heat up the pins enough to melt solder onto it, it never got hot enough. As it turns out, the breadboard was absorbing heat from the pins. As soon as I took it out of the breadboard, the solder melted on perfectly. As for the code, I had forgotten that bash is a lot less straightforward than python. I couldn't get a for loop to work, so I had to make a makeshift for loop using "until". I also found a useful docement online showing which pins on the cobler corresponded to which gpio in the code.

### Code

https://github.com/vpearce14/Engineering_4_Notebook/blob/master/Scripts/GPIOpins.sh

## GPIO Python

### Lessons Learned

GPIO Python was an assignment where I had to turn an LED on and off using Pyhton. Google was my best friend in this assignment. Sourceforg.net was most helpful, as it showed me the basics of setting up the GPIO. Mostly the issue lied in 

### Code

https://github.com/vpearce14/Engineering_4_Notebook/blob/master/Scripts/GPIOpython.py


## GPIO SSH

### Lessons Learned

This one was pretty easy once I got the ssh to connect, as the script was the same as gpio bash. I had to do some googling to find that the user and hostname were just the device and username that is displayed in terminal. Both devices also have to be connected to the same wifi.

## Hello Flask

### Lessons Learned

This was just a simple introduction to flask, where "Hello world!" was printed out on a webpage.

### Code

https://github.com/vpearce14/Engineering_4_Notebook/blob/master/Python/Flask/hello_world/app.py

## Flask GPIO

### Lessons Learned

This assignment was a massive pain. It was hard to get the webpage up, hard to put it all together, and hard to have a backround imge actually load. The assignment was seemingly simple: control two LEDs from a single webpage. Check boxes were obvious way to go, as they could actually display if they had already been pressed or not. To have them be checked at the right times, it's easiest to put the "Checked" qualifier in an if statement within the html page. 

### Code

https://github.com/vpearce14/Engineering_4_Notebook/tree/master/Python/Flask/gpio

## GPIO I2C

### Lessons Learned

In this assignment, I gathered acceleration data and printed it on the screen, each axis on a seperate line.

### Code

https://github.com/vpearce14/Engineering_4_Notebook/blob/master/Python/shapes.py

## Headless

### Lessons Learned

Things can run at startup!!!

### Code

https://github.com/vpearce14/Engineering_4_Notebook/blob/master/Python/accell.py

## Pi camera

### Lessons Learned

For some reason, my pi would freeze every time it tried to take a picture. I tried looking at the pi logs but didn't find anything. It only worked when I switched the board itself. I still can't figure out why that helped, but I'm glad the issue is fixed.

### Code

https://github.com/vpearce14/Engineering_4_Notebook/blob/master/Python/camera_test01.py
https://github.com/vpearce14/Engineering_4_Notebook/blob/master/Python/camera_test02.py
https://github.com/vpearce14/Engineering_4_Notebook/blob/master/Python/camera_test03.py

### Media

## Hack your stuff

### Lessons Learned

So for this one I was supposed to take an alarm and rewire it to turn on through a pi and an external output. I decided to use a poteniometer. I was hoping to get an actual analog reading from it, but according to the internet, Pis are not capable of analog reading through gpio without a chip that I couldn't find in the Sigma lab. Fortunately the potentiometer can work as a digital input, so 

### Code

https://github.com/vpearce14/Engineering_4_Notebook/blob/master/Python/hack.py

### Media

## Parent detector

### Lessons Learned

This time I made a motion-detector camera system. It scares me how easy it would be for my parents to actually create and implement one of these things.

### Code

https://github.com/vpearce14/Engineering_4_Notebook/blob/master/Python/parent-detector.py

### Media

## Stop motion

### Lessons Learned

In this assignment, I created a system where the press of a button would take a picture, then name it numerically. Then I took the images and compiled them into a video. At least, that's what was supposed to happen. For some reason it would only take two or three frames. I downloaded a program to make the animation smaller, but it still didn't work. 

### Code

https://github.com/vpearce14/Engineering_4_Notebook/blob/master/Python/StopMotion.py

### Media

