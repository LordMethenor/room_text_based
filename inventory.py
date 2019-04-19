import numpy
import scipy   
from room import Room
class Inv():

    def __init__(self, inv_name, capacity, inv_type):
        self.name = inv_name
        self.capacity = capacity
        self.items = []
        self.type = inv_type   
    #adding in an item generator would probably be the best way to do this. It would allow us to put in factors such as difficulty/level, element,
    def spawn_item(self, item_ID):
        #I think the best way to do inventories is probably lists of objects, not dictionaries. I researched dictionaries, and it seems they are good at storing multiple pieces of info about a singular item, but I think a class would better accomplish this for generation, sorted from an ITEM class in MELEE, RANGED, TRADE, ARMOR, etc subclasses)
        #Item ID is how objects of the item class are designated and generated. We use the item class and subclasses to generate them and then use these unique random identifiers to call them, as opposed to storing and transferring dictionaries 
        items_counter = 0
        for i in range(len(self.items)):
            items_ID = self.items[i]
            item_counter += items_ID.get_value()

        items_ID.num
        if len(self.items)<self.capacity:
            self.items.append(item_ID)
        else:
            return 0
    def add_item(self, item_ID):
        #Add item ignores the capacity. The capcity is only used to stop too much loot from spawning, but mob drops being added to the room or players dropping items shouldn't count against the quantity.
        self.items.append(item_ID)
    def list_items(self):
        print("\n")
        #This text depends on the inventory type. If player, it will state it is a player inventory. If it is loot or mob drops, it will state that, etc. It could also inform on the amount of remaining space.)
        print("Items: ")
        for i in range(len(self.items)):
            print("\n")
            item_ID = self.items[i]
        # isn't working    print("{}- {}".format((i+1), item_ID.get_the_basics))
        print("\n")
        print("Select an item: ")
        command = input("> ")
        try:
            if command.isdigit():
                command = int(command)
            else:
                null
            item_ID = self.items[command]
            print(item_ID.get_description)
        except:
            print("Please try again with a listed numerical value.")

class Item():
    #in the future, the general item will be broken into subclasses, like melee, food, armor, etc)
    #item_DICT can be used to add predetermined attributes. Some, like name, will be defined differently in different items. This is basically a flexible catch-all
    #rarity will
    def __init__(self, item_value, item_ID, item_Name, item_Rarity):
        #random normality, fix all item pulling stuff
        numpy.random.normal(loc=0.0, scale=1.0, size=None)
    def get_the_basics(self):
        rarity = self.dictnry['rarity']
        spec = self.dictnry['spec']
        return "{} ({}, {})".format(self.name, spec, rarity)
        
    def get_description(self):
        description = self.dictnry['description']
        return description
    
    def get_name(self):
        return self.name
class Normalize():
    # this is how random values are generated. They are generated on a normal distribution, with a mean as the 'base' spec and the standard deviation set to 15% of the mean by default but changeable. If an item with a certain rarity predetermined is generated, the returned result will specifically obey that. Values less than 0 are also eliminated.
    def __init__(self, mean, alt_deviation, minimum, rarity):
        self.mean = mean
        try:
            self.rarity = rarity
        except:
            self.rarity = 0
        try:
            self.devation = alt_deviation
        except:
            self.deviation = .15 * self.mean

    def draw_norm(self):
        draw_loop = True
        while draw_loop = True:
            output_return = numpy.random.normal(loc=self.mean, scale=self.deviation, size=None)
            if output_return >= self.rarity:
                draw_loop = False
            else:
                pass
        return output_return
class Rarity_Check(Normalize):

    def __init__(self, mean, alt_deviation, check_value):
        Normalize.__init__(self, mean, alt_deviation)
        self.value = check_value
    def check_rarity():
        return scipy.stats.norm(self.mean, self.deviation).cdf(check_value) 
