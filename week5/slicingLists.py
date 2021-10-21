#!/usr/bin/python3
age = [10, 12, 14, 16, 18, 20, 22, 24, 26]
#print(type(age))
#print(age[9])

# start with the index at the first number
# go up to the (second number-1)
print(age[0:3]) # 10, 12, 14
print(age[2:3]) # 14
print(age[1:5]) # 12, 14,16, 18
print(age[2:8]) # 14 ... 24
print(age[8:9])
print(age[-1])
print(age[-4])
print(age[-9]) # same as age[0]

names = "jane john peter susan"
namesList = names.split(' ')
print(namesList)
date = "10/20/2021".split('/') # [10, 20, 2021]
print(date)
print(int(date[0]) + int(date[1]))


