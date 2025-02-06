import random

random_number = random.randint(1, 100)

attempts = 10

print("Welcome to the Guessing Game!")
print("I have randomly chosen a number between 1 and 100.")
print(f"You have {attempts} attempts to guess it. Good luck!")

for i in range(attempts):
    attempts_left = attempts - 1
    
    try:
        guess = int(input(f"Attempt {i+1}/{attempts}. Enter your guess: "))
    except Error:
            print("Please enter a valid number.")
            continue
    
    if guess == random_number:
        print(f"Congratulations! You've guessed the number {random_number} correctly!")
        break
    elif guess < random_number:
        print(f"Your guess is too low. {attempts_left-1} attempts left.")
    else:
        print(f"Your guess is too high. {attempts_left-1} attempts left.")

else:
    print(f"Sorry, you've used all {attempts} attempts. The correct number was {random_number}.")
