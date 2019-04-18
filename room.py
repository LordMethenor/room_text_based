class Room():

    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.room_loot = {}
    def set_description(self, room_description):
        self.description = room_description

    #def loot_inv(self):
        #name_dict = {}        
        #inv_name = self.name.append(" Loot")
        #name_dict['inv_name'] = inv_name
        #name_dict['inv_name'] = Inv(self, inv_name, 3, 'Loot')
        #get object names working, add items and stuff
    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def set_name(self, room_name):
        self.name = room_name

    def describe(self):
        print( self.description )

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print( self.name )
        dash = ""
        for i in self.name:
            dash += "-"
        dash += '----'
        print(dash)
        print( self.description )
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is {}.".format(direction))
        print("")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way. ")
            return(self)
        