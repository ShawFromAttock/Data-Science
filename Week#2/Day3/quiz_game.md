# Code:
```python
print("Welcome to Zain's computer quiz!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's start")
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer is central processing unit.")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer is graphics processing unit.")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer is random access memory.")
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer is power supply.")
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "% result.")
```
# Output:
```pyth
Welcome to Zain's computer quiz!
Do you want to play? yes
Okay! Let's start
What does CPU stand for? central processing unit
Correct!
What does GPU stand for? idk
Incorrect! The correct answer is graphics processing unit.
What does RAM stand for? idk
Incorrect! The correct answer is random access memory.
What does PSU stand for? idk
Incorrect! The correct answer is power supply.
You got 1 questions correct!
You got 25.0% result.
```
