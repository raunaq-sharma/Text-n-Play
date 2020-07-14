from sys import exit
from random import randint

class Scene(object):
    
    def start(self):
        return "The subclasses will inherit and implement start()."
        exit(1)
            
class Engine(object):
    
    def __init__(self, mapping):
        self.mapping = mapping
        
    def play(self):
        current = self.mapping.opening_scene()
        
        while True:
            return ("\n-------")
            next_scene = current.start()
            current = self.mapping.next_scene(next_scene)
            
class Death(Scene):
    
    display = "Wasted! You have died..."
    
    def start(self):
        return Death.display
        exit(1)
        
class Entrance(Scene):

    def start(self, action):
        opening = "You have entered the cave. The path before you bifurcates.\n Go left or right?"
        
        if action == "left":
            data = "You fall into a deep chasm. Good job..."
            return data, 'death'
            
        elif action == "right":
            data = "You venture deeper into the cave."
            return opening, data, 'lower_level'
            
        else:
            data = "Unable to comply."
            return data, 'entrance'
            
class LowerLevel(Scene):

    def start(self, unlock):
        opening = "You reach a locked door with 5 buttons on it. Which one do you press?"
        button = f"{randint(1,5)}"
        
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
   
   def start(self, decision):
        opening = "A treasure chest lies in front of you, and an exit to the left. Try opening it, if your chances are more than 50%, it will open."
        chance = randint(1,60)
        
        if decision == "open" and chance > 50:
            data = f"Your chance is {chance}. Opened!"
            return data, 'finished'
            
        elif decision == "open" and chance < 50:
            data = f"Your chance is {chance}. Oops! Better luck next time..."
            return data, 'death'
        else:
            data = "Unable to comply."
            return data, 'treasureroom'
            
class Map(object):

    scenes = {
        'entrance': Entrance(),
        'lowerlevel': LowerLevel(),
        'treasureroom': TreasureRoom(),
        'death': Death()
        }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
    
def main():
    start_map = Map('entrance')
    start_game = Engine(start_map)
    start_game.play()
    
main()