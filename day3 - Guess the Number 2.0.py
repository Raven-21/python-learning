# Generate a random number
import random
number = random.randint(1,100)
print(number)

# Number of records
count = 0
chance = 10

# Show count
def show_count(current_count):
    if current_count == 1:
        print(f"You guessed it {current_count} time")
    else:
        print(f"You guessed it {current_count} times")

# Show remaining chances
def show_chance(current_chance):
    if current_chance > 1:
        print(f"You have {current_chance} more chances")
    elif current_chance == 1:
        print("You only get 1 chance. Keep it up!")
    else:
        print("Sorry! Game Over")
        print(f"The answer is {number}")

# Determination (A higher-order function calls a lower-order function)
def check_guess(current_guess,current_number, current_count, current_chance):
    if current_guess > current_number:
        print("Too high")
        show_count(current_count)
        show_chance(current_chance)
        return False
    elif current_guess < current_number:
        print("Too low")
        show_count(current_count)
        show_chance(current_chance)
        return False
    else:
        print("You guessed it right ✔")
        if current_count == 1:
            print(f"Congratulations!!! ^v^\nYou just guessed it 1 time!")
        else:
            show_count(current_count)
        return True

# Game over (no chance)
def is_game_over(current_chance):
    return current_chance == 0

print("Welcome to Guess the Number!")
print("Please enter a number between 1 and 100")
print("You have 10 chances. Good luck!")
while True:
# Get user input
    try:
        guess = int(input("\nGuess the number: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100!")
        continue

    count += 1
    chance -= 1
    if check_guess(guess, number, count, chance):
        break
    if is_game_over(chance):
        break