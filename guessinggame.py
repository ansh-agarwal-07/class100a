import random 

print("number gussing game")
number = random.randint(1,9)
chances = 0
print("guess a number between 1 and 9")
while chances < 5:
    guess = int(input("enter your guess:- "))
    if guess == number:
        print("congratulations!!! You have successfully guessed")
        break
    elif guess < number:
        print("Your guess was too low!")    
    else:
        print("Your guess was too high!")    
    chances +=1    
if not chances < 5:
    print("You lost!!!You have failed to guess the number")