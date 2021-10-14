#!/usr/bin/python3
# and/or
grade = eval(input("Enter grade: "))
# validate input
# put some lines in here to make your program robust
if (grade >= 90) and (grade <= 100):
    print("Grade is 'A'")
elif (grade >= 80) and (grade < 90):
    print("grade is 'B'")
elif (grade >= 70) and (grade < 80):
    print("grade is 'C'")
else:
    print("grade is 'F'")

