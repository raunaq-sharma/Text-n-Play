from sys import exit
from random import randint

class Scene(object):
    
    def start(self):
        print ("The subclasses will inherit and implement start().")
            exit(1)
            
class Engine(object):
    
    def __init__(self, mapping):
        self.mapping = mapping
        
    def play(self):
        current = self.mapping.opening()
        
        while True:
            print ("\n-------")
            next_scene = current.start()
            current = self.mapping.next_scene(next_scene)
            
class Death(Scene):
    
    display = "You have died..."
    
    def start(self):
        print Death.display
        exit(1)
        
class Entrance(Scene):

    def start(self, action):
        data = "You have entered the cave. The path before you bifurcates.\n Go left or right?"
        return data
        
        if action == "left"
            data = "You fall into a deep chasm. Good job..."
            return data, 'death'
            
        elif action == "right"
            data = "You venture deeper into the cave."
            return data, 'lower_level"
            
        else:
            data = "Unable to comply."
            return data, 'entrance'
            
class LowerLevel(Scene):

    def start(self, unlock):
        data = "You reach a locked door with 5 buttons on it. Which one do you press?"
        button = f"{randint(1,5)}"
        return data
        
        if unlock == button:
            data = "Gate unlocked! You venture forth..."
            return data, 'treasure_room'
            
        elif unlock != button:
            data = "A trapdoor opens below you, and you begin to fall."
            return data, 'death'
            
        else:
            data = "Unable to comply."
            return data, 'lowerlevel'
            
class TreasureRoom(Scene):
    