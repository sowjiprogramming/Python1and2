# import module
import random
# Create variable for random number
number = random.randint(1,10)

# Asking and storing name
name = input("Enter your name: ")
# Ask user to guess
guess = int(input("guess a number between 1-10: "))
print (number, "my number")                                 
# Tell user whether they are right or wrong
if guess == number:
    print(name,"you guessed it right!")
elif guess <= 10 and guess != number:
    print(name,"your guess is wrong.")
else:
    print(name,"your guess is invalid.")