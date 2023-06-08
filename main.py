import random
import colorama

# Initialize colorama
colorama.init()

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess the number between 1 and {x}: '))
        print()

        if guess == random_number:
            # Print the success message in green color
            print(colorama.Fore.GREEN + f"You got it! It's {random_number}")
        else:
            # Print the failure message in red color
            print(colorama.Fore.RED + "Sorry, try again :(")

# Call the guess function
guess(10)

# Reset the colorama settings
colorama.deinit()


