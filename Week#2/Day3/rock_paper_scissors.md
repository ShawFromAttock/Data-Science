# Code:
```python
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

input_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if input_choice > 2 or input_choice < 0:
    print("You typed an invalid number, You Lose!")
else:
    list = [rock, paper, scissors]
    print(list[input_choice])

    com_choice = random.randint(0, 2)
    print("Computer chose:")
    print(list[com_choice])
    if com_choice == input_choice:
        print("Draw")
    elif input_choice == 0 and com_choice == 2:
        print("You Won!")
    elif input_choice == 2 and com_choice == 0:
        print("You lost!")
    elif com_choice > input_choice:
        print("You lost")
    elif input_choice > com_choice:
        print("You Win")
```
# Output:
```python
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.0

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer chose:

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Draw
```
