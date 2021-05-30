import random

number = 5

chance=0

while chance < 5:
    guess=int(input("enter a guess between 1 and 9: "))
    if guess==number:
        print("Congrats! Your guess is right !")
        break
    elif guess<number:
        print(" Uh, no... Your guess was too low.... Hint: The number is higher than ",guess)
    else:
        print("aaaa, your guess was too high. Hint : The number is lower than ",guess)
if chance>5:
    print( "No ! You lose! The number was ",number )