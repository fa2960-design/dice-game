import random

# options=("r","p","s")#it is in tuple form so that it csnnot be changed


ROCK="r" #THIS IS A CONSTANT VARIABLE which helps to make the code more readable
PAPER="p"
SCISSORS="s"
emojis={"ROCK":"🪨","PAPER":"📄","SCISSORS":"✂️"}
print("welcome to rock ,paper ,scissors game!")
choices=tuple(emojis.keys()) #this will create a tuple of the keys from the emojis dictionary so no need to manually type options


def get_user_choice():
    while True:
        user_choice=input("enter rock ,paper or scissors(r/p/s): ").lower()
        if user_choice not in choices:
            print("invalid input lol")
            continue    #this will take the user back to the start of the loop if input is invalid to avaoid crashing at line 15 
        else:
            return user_choice


def display_choices(user_choice,computer_choice):
    print(f"you chose  {emojis [user_choice]}   and computer chose   {emojis [computer_choice]}")


def determine_winner(user_choice,computer_choice):
    

    if user_choice==computer_choice:
        print("its a tie!")

    elif (user_choice==ROCK and computer_choice==SCISSORS) or (user_choice==PAPER and computer_choice==ROCK) or (user_choice==SCISSORS and computer_choice==PAPER):
        print("hurray you win!")

    else:
        print("opps you loose!")
    


def play_game():

  while True:
    user_choice=get_user_choice()

    computer_choice=random.choice(choices)

    display_choices(user_choice,computer_choice) 

    determine_winner(user_choice,computer_choice)
    
    play_again=input("do you want to play again? (y/n): ").lower()  
    if play_again=="n":
        print("thanks for playing! goodbye!")
        break


play_game()







    
    
   