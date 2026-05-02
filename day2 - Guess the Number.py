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

while True:
# Get user input
    guess = int(input("\nGuess the number:"))
    count += 1
    chance -= 1
# Determination
    if guess > number:
        print("Too high")
        # Change of records
        if count == 1:
            print(f"You guessed it {count} time")
        else:
            print(f"You guessed it {count} times")
        # Change of chances
        if (chance < 10) and (chance > 0) and chance != 1:
            print(f"You have {chance} more chances")
        elif chance == 1:
            print("You only get one chance\nKeep it up!")
        else:
            print("Sorry! You didn't guess correctly within the allotted number of attempts. - -!")
            print(f"The answer is {number}")
            break
    elif guess < number:
        print("Too low")
        # Change of records
        if count == 1:
            print(f"You guessed it {count} time")
        else:
            print(f"You guessed it {count} times")
        # Change of chances
        if (chance < 10) and (chance > 0) and chance != 1:
            print(f"You have {chance} more chances")
        elif chance == 1:
            print("You only get one chance\nKeep it up!")
        else:
            print("Sorry! You didn't guess correctly within the allotted number of attempts. - -!")
            print(f"The answer is {number}")
            break
    else:
        print("You guessed it right ✔")
        if count == 1:
            print(f"Congratulations!!! ^v^\nYou just guessed it {count} time")
        else:
            print(f"You guessed it {count} times")
        break