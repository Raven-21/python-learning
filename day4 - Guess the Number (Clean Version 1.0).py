import random

# -------------------------
# Initialization
# -------------------------
number = random.randint(1,100)
count = 0
chance = 10
#print(number)

print("Welcome to Guess the Number!")
print("Please enter a number between 1 and 100.")
print("You have 10 chances. Good luck!")

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
        print("You only get 1 chance. Keep it up!")

def show_game_over(answer):
    print("Sorry! Game Over! - -!")
    print(f"The answer is {answer}.")

# -------------------------
# Logic Layer
# -------------------------
def check_guess(current_guess,current_number, current_count):
    if current_guess > current_number:
        print("Too high.")
        show_count(current_count)
        return False
    elif current_guess < current_number:
        print("Too low.")
        show_count(current_count)
        return False
    else:
        print("You guessed it right. ✔")
        if current_count == 1:
            print("Congratulations!!! ^v^\nYou just guessed it 1 time!")
        else:
            show_count(current_count)
        return True

# -------------------------
# Main Program
# -------------------------
while True:
    guess = get_guess()

    if guess is None:
        continue

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100!")
        continue

    count += 1
    chance -= 1

    # Determine Result
    if check_guess(guess, number, count):
        break

    # Show Remaining Chance
    show_chance(chance)

    # Game Over Condition
    if chance == 0:
        show_game_over(number)
        break