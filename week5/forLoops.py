#!/usr/bin/python3
# when you know the number of items to loop thru
import time

def add(a, b):
    return a+b


result = 9
if (result > 10):
    print(result)

colors = ['red', 'blue', 'green', 'yellow']
for c in colors:
    print(c)
    time.sleep(.5)

for i in range(10):
    print(i)

print("********")    

for k in range(1,10):
    print(k)

