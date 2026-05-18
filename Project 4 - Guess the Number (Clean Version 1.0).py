import random

# -------------------------
# Initialization
# -------------------------
print("Welcome to Guess the Number! 😀😀😀")
print("Please enter a number between 1 and 100.")

def choose_difficulty():
    while True:
        choice = input(
            "\nChoose Difficulty:\n"
            "1. Easy (10 Chances)\n"
            "2. Hard (5 Chances)\n"
            "Select: "
        )
        if choice == "1":
            return 10
        elif choice == "2":
            return 5
        else:
            print("\nPlease choose 1 or 2.")

# -------------------------
# Input layer
# -------------------------
def get_guess():
    try:
        current_guess = int(input("\nGuess the number: "))
        return current_guess
    except ValueError:
        print("Please enter a valid number!")
        return None

# -------------------------
# Presentation Layer
# -------------------------
def show_count(current_count):
    if current_count == 1:
        print(f"You guessed it {current_count} time.")
    else:
        print(f"You guessed it {current_count} times.")

def show_chance(current_chance):
    if current_chance > 1:
        print(f"You have {current_chance} more chances.")
    elif current_chance == 1:
        print("You only get 1 chance. Keep it up! 🦾🦾🦾")

def show_game_over(answer):
    print("Sorry! Game Over! 😥😥😥")
    print(f"The answer is {answer}.")

# -------------------------
# Logic Layer
# -------------------------
def check_guess(current_guess,current_number, current_count):
    if current_guess > current_number:
        print("Too high. ❌")
        show_count(current_count)
        return False
    elif current_guess < current_number:
        print("Too low. ❌")
        show_count(current_count)
        return False
    else:
        if current_count == 1:
            print("Unbelievable!!! 😮😮😮 You just guessed it right in 1 time! ✅")
        else:
            print("Congratulations! 😁😁😁 You guessed it right. ✅")
            show_count(current_count)
        return True

# -------------------------
# Game Layer
# -------------------------
def play_game():
    number = random.randint(1, 100)
    count = 0
    chance = choose_difficulty()
    history = []

    print(f"You have {chance} chances. Good luck! 😉")
    print(number)

    while True:
        guess = get_guess()
        if guess is None:
            continue
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100!")
            continue

        # Record History
        history.append(guess)

        count += 1
        chance -= 1

        # Determine Result
        if check_guess(guess, number, count):
            print("Guess History: ", history)
            break

        # Show Remaining Chance
        show_chance(chance)

        # Game Over Condition
        if chance == 0:
            show_game_over(number)
            print("Guess History: ", history)
            break

        print("Guess History: ", history)

def play_again():
    while True:
        choice = input("\nWould you like to play again? (y/n): ")
        if choice == "y":
            return True
        elif choice == "n":
            print("\nThank you for playing! 😀")
            return False
        else:
            print("Please enter a yes or no!")

# -------------------------
# Main Program
# -------------------------
while True:
    play_game()

    if not play_again():
        break