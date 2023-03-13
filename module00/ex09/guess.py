import random
import sys
print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
secret = random.randint(1, 99)
#secret = 42
i = 0
while 1:
    i += 1
    num = input("What's your guess between 1 and 99?\n>> ")
    try:
        guess = int(num)
    except:
        if num == "exit":
            sys.exit("Goodbye!")
        else:
            print("That's not a number.")
            continue
    if guess == secret:
        if secret == 42:
            print("The answer to the ultimate question on life, the universe and everything is 42.")
        if i == 1:
            print("Congratulations! You've got it on your first try!")
        else:
            print("Congratulations, you've got it!")
            print("You won in " + str(i) + " attempts!")
        sys.exit()
    elif guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
        