# Multiplayer Dice Game



import random
def roll():

    min_value=1
    max_value=6

    roll=random.randint(min_value, max_value)
    
    return roll

# value)=roll()
# print(value
while True:
    players=input("enter the nummber of players(1-4):")    #you enter the number of players here
    if players.isdigit():                                  #this is to check if the input is a digit
        players=int(players)                               #this will convert the string to integers
        if 1<= players<=4:                                 #this checkes if the numbers of players are between 1 and 4
            break                                          #this will break the loop if the range of num of players is achieved
        else:
            print("please enter a number betwween  1 and 4")
    else:
        print("invalid input")         
# print(players)







max_score=50                                              #this is the maximum score to win the game
players_scores=[0 for i in range(players)]                #create a list to store each players scores with each staring at 0


# print(players_scores)

while max(players_scores)<max_score:                     #this will check if the maximum score of any player is less than the max score to win the game
    for player_idx in range(players):                    #this will loop through each player when its his turn and satisfy the conditions
        print("\n player number",player_idx +1, "turn has just started!\n")                    #thsi will print the current number of the player whoose turn is it and also add line breaksfor better readerbility,we add 1 to player_idx because index starts from 0
        print("your total score is : ",players_scores[player_idx],"\n")                       #this will print the total score of the active player
        current_score=0  
        
        
                                                                    #this will keep track of the current players score
        while True:
            should_continue_rolling=input("do you want to roll again?(y):")                    #this will ask the user if he wants to roll again 
            if should_continue_rolling.lower()!='y':                                           #this will check if the user input is not equal to y
                break
            
            value=roll()                                                                     #this will call the roll function

            if value==1:                                                                      #thi will check if the rolled value is 1
                print("you rolled a 1!,your score is back to 0 sorry your trun is over haha")
                current_score=0                                                       #this will reset the current score after rollling to one so that itdoes not add to the total score of the other players 
                break                                                                    #this will break the loop for the current player and move to the next player
            else:
                current_score+=value                                                    #this will add the rolled die to the  current score
                print("you rolled a :",value)   

            print("your score is now ",current_score)      
        players_scores[player_idx]+=current_score                                                  #this will add the the current score to the active player total score
        print("hey,your total score is now:",players_scores[player_idx])                          #this will print the total scores of the active player


max_score=max(players_scores)                                                           #this will get the maximum score from the list of players scores
winner_idx=players_scores.index(max_score)                                                 #this will get the index of the player with the maximum score
print("player number",winner_idx +1,"is the winner because he got the highest scores of:",max_score)   #this will print the winner and his scores,we add 1 to the winner because the index starts from 0




            
                 

