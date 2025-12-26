import random


attempt=0
number_to_guess=random.randint(1,100)
playing=True
while playing:
    try:
        user_input = int(input("guess a number between 1 and 100: "))
       
        attempt = attempt + 1


        if user_input < number_to_guess:
          
            print("too low kiddo.try again")    

        elif user_input > number_to_guess:
            print("too high kiddo,try again")  
        

        else:
            print(f"congratulations kiddo,you guesss the {number_to_guess} in {attempt} attempts")
            break

    except ValueError:
        print("invalid input, please enter an integer.")


 