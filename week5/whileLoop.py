#!/usr/bin/python3
import time
import random

i = 1
while i < 10:
    print(i)
    #time.sleep(1)
    i += 1

# do something here
response = 'y'
while response == 'y': #as long as
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    
    print(die1, die2)
    print()
    response = input("Hit y to continue: ")

colors = ['red', 'blue', 'green', 'yellow']
colors.random()