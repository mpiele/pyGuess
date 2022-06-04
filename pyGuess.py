import random

def start_guess(min, max):
    guess = random.randint(min, max)
    hint = random.randint(min, max)
    type = ""
    if guess == hint:
        type = "same"
    if guess < hint:
        type = "lower"
    if guess > hint:
        type = "higher"
    print("Your hint is {}, the number is lower, higher or same as the hint?".format(hint))
    print("1. same")
    print("2. lower")
    print("3. higher")
    
    answer = input()
    if answer == type:
        print("You win! The number was {}".format(guess))
    if answer != type:
        print("You lose! The number was {}".format(guess))
