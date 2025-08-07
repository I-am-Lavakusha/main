#this is a small program to guess a number
import random
def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to 'Guess the Number'!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")
if __name__ == "__main__":
    guess_the_number()
# This program generates a random number between 1 and 100 and allows the user to guess