from sys import exit
from random import randint
            
def main():
    
    Entrance()
   
def TreasureRoom():
    opening = "A treasure chest lies in front of you, and an exit to the left. Try opening it, if your chances are more than 50%, it will open."
    chance = randint(1,75)
    print(opening, chance)
    decision = input(">treasureroom ")
    if decision == "open" and chance > 50:
        data = f"Your chance is {chance}. Opened!"
        next_open = data, 'finished'
        
    elif decision == "open" and chance < 50:
        data = f"Your chance is {chance}. Oops! Better luck next time..."
        next_open = data, Death
    else:
        data = "Unable to comply."
        next_open = data, TreasureRoom
    
    print(data)
    return next_open[1]()
    
        
def LowerLevel():
    opening = "You reach a locked door with 5 buttons on it. Which one do you press?"
    button = f"{randint(1,5)}"
    print(opening, button)
    unlock = input(">lowerlevel ")
    
    if unlock == button:
        data = "Gate unlocked! You venture forth..."
        next_open = data, TreasureRoom
        
    elif unlock != button:
        data = "A trapdoor opens below you, and you begin to fall."
        next_open = data, Death
        
    else:
        data = "Unable to comply."
        next_open = data, LowerLevel
    
    print(data)
    return next_open[1]()

def Entrance():
    
    opening = "You have entered the cave. The path before you bifurcates.\n Go left or right?"
    print(opening)
    action = input(">entrance ")
    
    if action == "left":
        data = "You fall into a deep chasm. Good job..."
        next_open = data, Death
        
    elif action == "right":
        data = "You venture deeper into the cave."
        next_open = data, LowerLevel
        
    else:
        data = "Unable to comply."
        next_open = data, Entrance
        
    print (data)
    return next_open[1]()

def Death():
    
    print("Wasted! You have died...")
    exit(1)
    
main()