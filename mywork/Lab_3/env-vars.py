#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3

import os

NAME = input("What is your name? \n")
AGE = input('What is your age? \n')
YEAR = input('What year are you at UVA? \n')

os.environ["NAME"] = NAME
os.environ["AGE"] = AGE
os.environ["YEAR"] = YEAR

print("Your name is " + os.environ["NAME"])
print("Your age is " + os.environ["AGE"])
print("Your year is " + os.environ["YEAR"])
