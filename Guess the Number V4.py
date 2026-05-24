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
# Input Layer
# -------------------------
def get_guess():
    try:
        current_guess = int(input("\nGuess the number: "))
        return current_guess
    except ValueError:
        print("Please enter a valid number!")
        return None

# -------------------------
# Logic Layer
# -------------------------
def check_guess(current_guess, current_number):
    if current_guess > current_number:
        return "high"
    elif current_guess < current_number:
        return "low"
    else:
        return "correct"

# -------------------------
# Presentation Layer
# -------------------------
def show_result(current_result, current_count):
    if current_result == "high":
        print("Too High. ❌")
    elif current_result == "low":
        print("Too low. ❌")
    else:
        if current_count == 1:
            print("Unbelievable!!! 😮😮😮 You just guessed it right in 1 time! ✅")
        else:
            print("Congratulations! 😁😁😁 You guessed it right. ✅")

def show_chance(chance):
    if chance > 1:
        print(f"You have {chance} more chances.")
    elif chance == 1:
        print("You only get 1 chance. Keep it up! 🦾🦾🦾")

def show_history(history):
    print("\nGuess History:")
    for record in history:
        print(f"{record['guess']} → {record['result']}")

def show_game_over(answer):
    print("Sorry! Game Over! 😥😥😥")
    print(f"The answer is {answer}.")

# -------------------------
# Game Layer
# -------------------------
def play_game():
    number = random.randint(1, 100)
    count = 0
    max_chance = choose_difficulty()
    history = []

    print(f"You have {max_chance} chances. Good luck! 😉")
    print(number)

    while True:
        # Get Input
        guess = get_guess()
        if guess is None:
            continue
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100!")
            continue

        count += 1
        remaining_chance = max_chance - count
        result = check_guess(guess, number)

        # Record History
        history.append({
            "guess": guess,
            "result": result
        })

        # Determine Result
        show_result(result, count)
        if result == "correct":
            show_history(history)
            break

        # Show Remaining Chance
        show_chance(remaining_chance)

        # Game Over Condition
        if remaining_chance == 0:
            show_game_over(number)
            show_history(history)
            break

        show_history(history)

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