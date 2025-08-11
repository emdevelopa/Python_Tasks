import random

secret_number = random.randint(1, 5)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 5git .")

guesses = 0

while True:
    try:
        guess = int(input("Take a guess:"))
        guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! you guessed the number {secret_number} in {guesses} tries!")
            break
    except ValueError:
        print("Pease enter a valid integer.")

 

