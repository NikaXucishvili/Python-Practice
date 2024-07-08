#!/usr/bin/env python3

def my_function():
	"""This is just some message"""
	global message
	message = "Hello everyone"
	print(message)
my_function()


name = input("Enter your name:\n")
print("Your name is " + name)

age = input("Enter your age:\n")
print("You are " + age + "years old")
age2 = int(age) + 50
print("In 50 years, you will be " + str(age2) + "years old") 


