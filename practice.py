#!/usr/bin/env python3

def my_function():
	"""This is just some message"""
	global message
	message = "Hello everyone"
	print(message)
my_function()


#name = input("Enter your name:\n")
#print("Your name is " + name)

#age = input("Enter your age:\n")
#print("You are " + age + "years old")
#age2 = int(age) + 50
#print("In 50 years, you will be " + str(age2) + "years old " + "Probably Dead..") 



#number = input("Please Enter a number between 1 and 10: ")

#if int(number) <= 10:
 #   print("A valid number was entered")
#else:
#    print("An invalid number was entered.")    
#print("This will always print.")


age = input("Please enter your age: ")
if int(age) >= 50:
	print("You are 50 or older.")
elif int(age) >= 18:
	print("You are an adult.")
else:
	print("You are not even an adult.")

print("This will always print.")
