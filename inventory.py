import numpy
import scipy   
from room import Room
from normal import Normalize
from normal import Rarity_Check

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
        item_counter = 0
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
                pass
            item_ID = self.items[command]
            print(item_ID.get_description)
        except:
            print("Please try again with a listed numerical value.")

class Item():
    #in the future, the general item will be broken into subclasses, like melee, food, armor, etc)
    #item_DICT can be used to add predetermined attributes. Some, like name, will be defined differently in different items. This is basically a flexible catch-all
    #rarity will
    def __init__(self, item_space, item_value, item_dev, item_ID, item_name, item_unit, item_rarity):
        #random normality, fix all item pulling stuff
        self.ID = item_ID
        self.mean = item_value
        self.name = item_name
        self.space = item_space
        #will be removed once subclasses are implemented.
        self.unit = item_unit
        try:
            self.dev = item_dev
        except:
            self.dev = 'null'
        try:
            self.rarity = item_rarity
        except:
            self.rarity = 'null'
        normal_spec = Normalize.(mean = self.mean, alt_deviation = self.dev, minimum = self.rarity)
        #get the standard dev and rarity generated by the normalization process
        self.spec = normal_spec
        try:
            if self.rarity >= 0:
                pass
            else:
                pass
        except:
            rarity_check = Rarity_Check(self, mean = self.mean, alt_deviation = self.dev, check_spec = self.spec)
            
    def get_the_basics:
        return "{} ({}, {})".format(self.name, spec, rarity)
        
    def get_description(self):
        description = self.dictnry['description']
        return description
    
    def get_name(self):
        return self.name
