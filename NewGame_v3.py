from sys import exit
from random import randint

Map = { 
        'death' : "Wasted! You have died...",
        'victory' : "Finished! You won!",
        'bad_input' : "Unable to comply.",
        'opening_1' : "You have entered the cave. The path before you bifurcates.\n Go left or right?",
        'action_left' : "You fall into a deep chasm. Good job...",
        'action_right' : "You venture deeper into the cave.",
        'opening_2' : "You reach a locked door with 5 buttons on it. Which one do you press?",
        'unlock' : "Gate unlocked! You venture forth...",
        'not_unlock' : "A trapdoor opens below you, and you begin to fall.",
        'opening_3' : "A treasure chest lies in front of you, and an exit to the left. Try opening it, if your chances are more than 50%, it will open.",
        'more_than_50' : "You're lucky. Opened!",
        'less_than_50' : "You're unlucky. Oops! Better luck next time..."
      }
      

def entrance(action):    
    
    if action == "right":
        data =  Map['action_right']
    elif action == "left":
        data = (Map['action_left'] + "\n" + Map['death'])
    else:
        data = Map['bad_input']
    
    return data
        
def lower_level(unlock):

    button = randint(1,5)
    if unlock  == 1:
        data = (Map['unlock'])
    else:
        data = (Map['not_unlock'] + "\n" + Map['death'])
    
    return data, button
     
def treasure_room(decision):     

    chance = randint(1,75)
    print(chance)
    if decision == "open" and chance > 50:
        data =  (Map['more_than_50'] + "\n" +  Map['victory'])
    elif decision == "open" and chance < 50:
        data = (Map['less_than_50'] + "\n" + Map['death'])
    else:
        data = (Map['bad_input'])
        
    return data
    