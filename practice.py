#!/usr/bin/env python3


### Functions 

"""def my_function():
	This is just some message
	global message
	message = "Hello everyone"
	print(message)
my_function()"""


#Enter your name + age

"""name = input("Enter your name:\n")
print("Your name is " + name)

age = input("Enter your age:\n")
print("You are " + age + "years old")
age2 = int(age) + 50
print("In 50 years, you will be " + str(age2) + "years old " + "Probably Dead..") """



### Enter a number between 1 and 10: #####

"""number = input("Please Enter a number between 1 and 10: ")

if int(number) <= 10:
   print("A valid number was entered")
else:
    print("An invalid number was entered.")    
print("This will always print.")"""



######## age adult older or not even adult 


""" age = input("Please enter your age: ")
if int(age) >= 50:
	print("You are 50 or older.")
elif int(age) >= 18:
	print("You are an adult.")
else:
	print("You are not even an adult.")

print("This will always print.")""" 


###Password Checker ################

"""import getpass

pswd = getpass.getpass('Password:')

print(pswd)"""

#### While loop ########

"""my_num = 1

while my_num <= 10:
	print(my_num)
	my_num = my_num + 1
else:
	print(my_num)"""


###for loops

"""foods = ["pizza", "tacos", "hamburger", "xinkali"]
for f in foods:
	print(f)

sentence = "Python is awesome!"
for c in sentence:
	print(c)

import random

counter = random.randint(5, 10)

number = 1
for i in range(counter):
	print(number)
	number += 1"""


### Tuples

"""heroes = ("The Batman", "Spider-Man", "The Joker", "Wonder Woman")
for h in heroes:
	print(h)
print(len(heroes))"""

## OS Operating system

import os

"""print(os.getcwd()) ##get current working directory 

os.rename("first.txt", "second.txt")"""

os.system('ls')

print("Your current working directory is: " + os.getcwd() + "\n\n")

print("The contents of this directory are: ")
os.system('ls')
