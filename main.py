from room import Room

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A large room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
dining_hall.link_room(kitchen, "north")

current_room = kitchen

while True:

    print("\n")
    current_room.get_details()
    current_name = current_room.get_name()
    print("What do you want to call the {}?".format(current_name))
    new_room_name = input("> ")
    current_room.set_name(new_room_name)
    current_name = current_room.get_name()
    print("The name has been changed to {}.".format(current_name))
    print("\n")
    current_room.get_details()    
    command = input("> ")
    current_room = current_room.move(command)