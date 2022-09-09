# Code:
```python
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_ans(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer is {answer}.")


def set_difficulty():
    level = input("Choose a difficulty, 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_ans(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess Again!")
game()
```
# Output:
```python
Welcome to the Number Guessing Game!
I am thinking of a number between 1 and 100.
Choose a difficulty, 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number
Make a guess: 50
Too low.
Guess Again!
You have 9 attempts remaining to guess the number
Make a guess: 70
Too low.
Guess Again!
You have 8 attempts remaining to guess the number
Make a guess: 80
Too high.
Guess Again!
You have 7 attempts remaining to guess the number
Make a guess: 75
Too low.
Guess Again!
You have 6 attempts remaining to guess the number
Make a guess: 76
Too low.
Guess Again!
You have 5 attempts remaining to guess the number
Make a guess: 72
Too low.
Guess Again!
You have 4 attempts remaining to guess the number
Make a guess: 71
Too low.
Guess Again!
You have 3 attempts remaining to guess the number
Make a guess: 79
Too high.
Guess Again!
You have 2 attempts remaining to guess the number
Make a guess: 78
You got it! The answer is 78.
```
