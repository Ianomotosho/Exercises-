# Write a Python program to guess a number between 1 to 9. 
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit. 
import random

# while loop
secret_number = random.randint(1,10)
while True:
    T = int(input('guess between 1 and 9: '))
    if T == secret_number:
        print('you got it right')
    else:
        print('na nana nana you got it wrong')

# for loop
Impossible = random.randint(1,10)
for items in range(1,10):
    choice = int(input('guess beetween 1 and 10: '))
    if choice == Impossible:
        print ('you got it right')
        break
    else:
        print('you got it wrong ha')