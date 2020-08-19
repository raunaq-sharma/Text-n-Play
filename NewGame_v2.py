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
      
def main():
    button = f"{randint(1,5)}"
    chance = randint(1,75)
    
    print(Map['opening_1'])
    action = input(">entrance: ")
    if action == "right":
        print(Map['action_right'])
    elif action == "left":
        status = "death"
    else:
        status = "death"
    
    print(Map['opening_2'])
    unlock = input(">lowerlevel: ")
    if unlock  == button:
        print(Map['unlock'])
    elif type(unlock) != int:
        print(Map['bad_input'])
    else:
        print(Map['not_unlock'], Map['death'], sep = "\n")
        
    print(Map['opening_3'])
    decision = input(">treasureroom: ")
    if decision == "open" and chance > 50:
        print(Map['more_than_50'], Map['victory'], sep = "\n")
    elif decision == "open" and chance < 50:
        print(Map['less_than_50'], Map['death'], sep = "\n")
    else:
        print(Map['bad_input'])
    
main() 