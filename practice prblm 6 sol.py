                                    # Guess the number

"""
Generate a random number from a to b. you and your friend have to guess the number between two numbers a and b
which are inputs taken from the user. Your friend is player 1 and he plays first. He will have to keep choosing
the number and program must have to tell whether the number is greater then the actual number or less then actual number.
Log the number of trials it took your friend to arrive to the number.
You play the same game and the person with minimum number of trails wins.

RANDOMLY GENERATE A NUMBER AND DON'T SHOW TO THE USER

random.randint - generate the random number between a and b

INPUTS :
Enter the value of a
4
Enter the value of b
13
OUTPUTS:

Player1 :
Please guess the number between 1 to 13

5
Wrong guess a greater number again

6
Correct you took three trails to guess the number

Player2 :
.
.
.
Correct you took 7 trails to guess the number

Player1 wins!
"""

import random

def Guessthegame(a, b, actual):
    guess = int(input(f"Guess a number between {a} and {b}\n"))
    nguess = 1
    while guess != actual:
        if guess < actual:
            guess = int(input(f"Enter a bigger number\n"))
            nguess +=1

        else:
            guess = int(input(f"Enter a smaller number\n"))
            nguess +=1

    print(f"You have guessed the number in {nguess} guesses\n")
    return nguess


if __name__ == '__main__':
    a = int(input("Enter the value of a\n"))
    b = int(input("Enter the value of b\n"))
    actual = random.randint(a, b)
    print("Player 1's turn\n")
    g1 = Guessthegame(a, b, actual)
    print("Player 2's turn\n")
    g2 = Guessthegame(a, b, actual)

    if g1 < g2:
        print("Player 1 won the match!\n")

    elif g2 > g1:
        print("Player 2 won the match!\n")

    else:
        print("It's a Tie\n")
