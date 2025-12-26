import random

playing=True
rolls=0
final_total=0
while playing:
    choices = input("Do you want to roll a dice?(y/n): ").lower()
    if choices == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        rolls +=1
        final_total += total
        print(f"you rolled {dice1} and {dice2}")
        print(f"your total roll was {total}")
    elif choices == "n":
        print(f"you rolled {rolls} times and you total roll was {final_total}.Thank you for playing my game kiddo!")
        break
    else:
        print("invalid input, try again")