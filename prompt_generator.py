
#guess the number game

#I made it so the computer progressively gets more annoyed when you need to keep guessing higher.
#I made it so it will ask you if you want to play again after you've gotten the right answer, and either start a new round or say goodbye.
#I put it in a nested loop so the number would generate random again.
#I add a count function so I could keep track of how many times the argument was true in a round. 


import random


while True:

    random_number = random.randint(1, 100)
    count_number = 0

    while True:
        guess = int(input("Guess a number from 1-100: "))

        if guess == random_number:
            print("That's it! Congrats!")
            break
            
        elif guess > random_number:
            print("Nope, lower!")

        elif guess < random_number:
            count_number += 1

            if count_number == 1:
                print("Nope, higher!")
            elif count_number == 2:
                print("Higher still!")
            elif count_number == 3:
                print("jfc HIGHER!")
            else:
                print("Higher.")
            continue

    again = input("Do you want to play again? y/n ").lower()
    if again == 'y':
        print("Okay, here we go!")
        continue
    elif again == 'n':
        print("Okay, bye!")
        break

