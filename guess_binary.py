import random

def prompt_for_number(LOWER, UPPER):
    LOWER = int(input("Lower bound: "))
    UPPER = int(input("Upper bound: "))
    x = random.randint(LOWER, UPPER)
    return x

number = prompt_for_number()
num_guess = 1
while True:
    guess = input("Guess number: ")
    if guess == number:
        print(f"Congrats, you guessed the number in {num_guess} tries!")
        break
    elif guess >= number:
        print("Your guess is too large!")
        print(f"Try a number between 1 and {guess}.")
        num_guess += 1
    else:
        print("Your guess is too small!")
        num_guess += 1
    

