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

asaki = input("Enter your age:\n")
print("You are " + asaki + "years old")
age2 = int(asaki) + 50
print("In 50 years, you will be " + str(age2) + "years old " + "Probably Dead..") 

"""

### Enter a number between 1 and 10: #####

"""number = input("Please Enter a number between 1 and 10: ")

if int(number) <= 10:
   print("A valid number was entered")
else:
    print("An invalid number was entered.")    
print("This will always print.")

"""

######## age adult older or not even adult 
""" age = input("Please enter your age: ")

try:
    age = int(age)  # Convert age input to an integer
    if age >= 50:
        print("You are 50 or older.")
    elif age >= 18:
        print("You are an adult.")
    else:
        print("You are not even an adult.")
except ValueError:
    print("Invalid input. Please enter a valid age.")

print("This will always print.")"""


###Password Checker ################

"""import getpass

pswd = getpass.getpass('Password:')

print(pswd)

#### While loop ########

my_num = 1

while my_num <= 10:
	print(my_num)
	my_num = my_num + 1
else:
	print(my_num)
"""

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
	number += 1
"""

### Tuples

"""heroes = ("The Batman", "Spider-Man", "The Joker", "Wonder Woman")
for h in heroes:
	print(h)
print(len(heroes))"""

## OS Operating system

"""import os

print(os.getcwd()) ##get current working directory 

###os.rename("first.txt", "second.txt")
os.system('ls')

print("Your current working directory is: " + os.getcwd() + "\n\n")

print("The contents of this directory are: ")
os.system('ls')

file = input("Enter a file name: ")

if os.path.isfile(file):
	print("The file exists,")
else:
	print("The file doesnt exist")
	print("creating it,,,")
	os.system('touch {}'.format(file))

"""
##### subprocess

"""import subprocess

svc = "sshd"

check_cmd = ["ps",
	    "-C",
	    svc]
	 
service_check = subprocess.call(check_cmd)
if service_check == 0:
	print("its running")
else:
	print("its not running")
	print("Starting it...")
	subprocess.call(["systemctl", "start", "sshd"])
	subprocess.call(check_cmd)

## Handling Exceptions

foods = ("Lasagna", "Ravioli", "Pizza")

try:
    foods[1] = "Macaroni"
except:
    print("There was an error.")

myfile = "file.txt"
try:
    file = open(myfile, "a")
except FileNotFoundError as e:
	print("The file was not found.")
	print(e)
	exit(1)

movies = ["The Matrix", "The Lord of the Rings", "The Avengers"]

for m in movies:
	file.write(m + "\n")
file.close()

ricxvebi = [0, 1, 2, 3, 4, 5]

for i in ricxvebi:
	print(i)"""

"""while True:
	ricxvi = input("Enter a number: ")
	ricxvi_int = int(ricxvi)

	if ricxvi_int % 2 ==0:
		print(f"{ricxvi_int} is even.")
		break
	else:
		print(f"{ricxvi_int} is odd. Please enter an even number.")"""


# Function to add two numbers
"""
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main function to take input from the user
def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
"""


###flask
"""from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def html_page():
    return render_template('site.html')

app.run(debug=True)
"""

class GameCharacter:
    def __init__(self, name, life):
        self.name = name
        self.life = life
    
    def attack(self):
        print(self.name + " kicks the enemy.")
    
    def life_check(self):
        if self.life <= 0:
            print(self.name + " was defeated!")
        else:
            print(self.name + " is still in the fight.")


class GameEnemy:
    def __init__(self, name, life):
        self.name = name
        self.life = life
    
    def attack(self):
        print(self.name + " attacks the heroes!")
    
    def life_check(self):
        if self.life <= 0:
            print(self.name + " was defeated!")
        else:
            print(self.name + " is still in the fight.")

# Instantiate game characters and enemies
player1 = GameCharacter("Roger", 100)
player2 = GameCharacter("Betty", 100)
enemy1 = GameEnemy("Bill", 150)
enemy2 = GameEnemy("Bob", 150)

# Example usage
player1.attack()
enemy1.life -= 50
enemy1.life_check()  # Check enemy1's life status
print("The enemy takes 50 damage, and has " + str(enemy1.life) + " life remaining.")

player2.attack()
enemy2.life -= 70
enemy2.life_check()  # Check enemy2's life status
print("The enemy takes 70 damage, and has " + str(enemy2.life) + " life remaining.")

