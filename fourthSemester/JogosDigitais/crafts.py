import random

crafts_num = int(input("How many space crafts do you wish? "))

while crafts_num < 2 or crafts_num > 10:
    crafts_num = int(input("Please, follow the range of 2 to 10: "))

def create_spacecrafts():
    """
    Creates a dictionary that will contain 'crafts_num' of spacecrafts objects with unique names.
    Args: 
        crafts_num: total crafts to make

    Returns:
        a dictionary where keys are unique spaceship names (based on letter in lowercase plus its names)    
    """
    crafts = {}
    start_letter = 'a'
    max_letter = chr(ord(start_letter) + crafts_num - 1)

    while ord(start_letter) <= ord(max_letter):
        name = input(f"Enter the name of the spacecraft that starts with '{start_letter}': ")
        crafts[start_letter] = SpaceCraft(name)
        start_letter = chr(ord(start_letter) + 1)    

    return crafts

class SpaceCraft:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.lasers = 9
        self.armor = 72
    
    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i lasers)" % (self.name, self.armor, self.lasers)
        else:
            return "%s (DEAD)" % self.name
        
    def fires_at(self, enemy):
        if self.lasers >= 1:
            self.lasers -= 1
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shots!")
            
    def hit(self):
        self.armor -= 18
        print(self.name, "has been hit")
        if self.armor <= 0:
            self.explode()
    
    def explode(self):
        self.alive = False
        print(self.name, "has exploded!")

crafts = create_spacecrafts()

while len(crafts) > 1:
    random.shuffle(crafts)
    for i in range(0, len(crafts), 2):
        craft1 = crafts[list(crafts.keys())[i]]
        craft2 = crafts[list(crafts.keys())[i + 1]]
        if craft1.alive and craft2.alive:
            craft1.fires_at(craft2)
            if craft2.alive:
                craft2.fires_at(craft1)

# Determine the winner
winner = None
for craft in crafts.values():
    if craft.alive:
        winner = craft.name
        break

print("The winner is:", winner)
