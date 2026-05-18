print("Welcome to Guess the Number!")
print("Please enter a number between 1 and 100")
print("You have 10 chances. Good luck!")

# Generate a random number
import random
number = random.randint(1,100)
#print(number)

# Number of records
count = 0
chance = 10

# Change of count
def show_count(current_count):
    if current_count == 1:
        print(f"You guessed it {current_count} time")
    else:
        print(f"You guessed it {current_count} times")

# Change of chance
def show_chance(current_chance):
    if current_chance > 1:
        print(f"You have {current_chance} more chances")
    elif current_chance == 1:
        print("You only get one chance. Keep it up!")
    else:
        print("Sorry! You didn't guess correctly within the allotted number of attempts. - -!")
        print(f"The answer is {number}")

while True:
# Get user input
    guess = int(input("\nGuess the number:"))
    count += 1
    chance -= 1
# Determination
    if guess > number:
        print("Too high")
        show_count(count)
        show_chance(chance)
        if chance == 0:
            break
    elif guess < number:
        print("Too low")
        show_count(count)
        show_chance(chance)
        if chance == 0:
            break
    else:
        print("You guessed it right ✔")
        if count == 1:
            print(f"Congratulations!!! ^v^\nYou just guessed it {count} time")
        else:
            print(f"You guessed it {count} times")
        break