#!/usr/bin/env python3

def my_function():
	"""This is just some message"""
	global message
	message = "Hello everyone"
	print(message)
my_function()
print(message)

print("Enter your name:")
name = input()
print(name)


