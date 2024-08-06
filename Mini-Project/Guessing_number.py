#Program For Guessing A Number

import random

def guess_number():
    score = 0
    attempts_allowed = 3

    print("Welcome to the Enhanced Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while True:
        number_to_guess = random.randint(1, 100)
        attempts = 0
        print(f"\nRound with {attempts_allowed} attempts allowed.")
        
        while attempts < attempts_allowed:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                elif guess < number_to_guess:
                    print("Your guess is too low. Try again.")
                elif guess > number_to_guess:
                    print("Your guess is too high. Try again.")
                else:
                    score += 1
                    attempts_allowed += 1
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    print(f"Your score is now {score}. You now have {attempts_allowed} attempts for the next round.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        if attempts == attempts_allowed and guess != number_to_guess:
            print(f"Sorry, you've used all {attempts_allowed} attempts. The number was {number_to_guess}.")
            print(f"Your final score is {score}.")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == 'yes':
                score = 0
                attempts_allowed = 3
            else:
                print("Thanks for playing! Goodbye!")
                break

if __name__ == "__main__":
    guess_number()
