import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

value = roll()


while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")
        
        
max_score = 50
# "_" - это значит, что значение переменной не будет использоваться (соглашение)
player_scores = [0 for _ in range(players)] 

print(player_scores)

while max(player_scores) < max_score:
    
    for player_idx in range(players):
        current_score = 0
        
        should_roll = input("Would you like to roll (y)? ")
        if should_roll.lover() == "y":
            break

        value = roll()
        if value == 1:
            print("You rolled a 1! Turn done!")
        else:
            current_score += value
            print("You rolled a:", value)
            
        print("Your score is:", current_score)