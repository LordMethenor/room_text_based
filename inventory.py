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
    def __init__(self, item_name, item_value, item_DICT):
        self.name = item_name
        self.value = item_value
        self.dictnry = item_DICT
#    def get_the_basics(self):
#also not working        return "{} ({}, {})".format(self.name,self.dictnry['spec'],self.dictnry['rarity'].if(item_DICT['rarity'] != 0))
    def get_description(self):
        return self.dictnry['description']
    def get_name(self):
        return self.name