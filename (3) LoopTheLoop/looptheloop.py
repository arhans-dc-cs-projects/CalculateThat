# Challenge 1 - Stopwatch
import time
count = 1
stop = int(input("Enter your stop number: "))

while stop > count-1:
  print(count)
  time.sleep(1)
  count+=1

# Challenge 2 - Countdown
start = int(input("Enter your start number: "))
count = 0

while count < start:
  print(start)
  time.sleep(1)
  start = start - 1

print("Blast off!")

# Challenge 3 - Guess My Number
import random
x = 0
number = random.randint(1, 100)

while True:
    play = None
    #print (number)
    x = x + 1
    guess = int(input("Guess the number from 1-100: "))
    if guess == number:
        print("You guessed the number.")
        print("You took",x,"guess/es." )
        play = input("Would you like to play again?")
        if play == "yes":
            number = random.randint(1, 100)
            pass
            x = 0
        if play != "yes":
            print("Thanks for playing!")
            break
    if number > guess:
        print("Too low! Guess again.")
    elif guess > number:
        print("Too high! Guess again!")
        
# Challenge 4 - Timetable Grid
for x in range(1, 11):
  for y in range(1, 11):
    print('{:3}'.format(x * y), end=' ')
  print()

