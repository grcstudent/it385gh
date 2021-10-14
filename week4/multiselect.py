#!/usr/bin/python3
grade = eval(input("Enter grade: "))
if grade >= 90: #91, 92...
    print("Grade is 'A'")
elif grade >= 80:
    print("Grade is 'B'")
elif grade >= 70:
    print("Grade is 'C'")
else:
    print("grade is 'F'")