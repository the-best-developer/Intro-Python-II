# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    ##################################################

    def get_current_room(self):
        print(self.current_room.name + "\n")
        print(self.current_room.description + "\n")
        return

    def set_current_room(self, input_text):
        switch_dict={
            "n": self.current_room.n_to,
            "s": self.current_room.s_to,
            "e": self.current_room.e_to,
            "w": self.current_room.w_to,
        }

        # Choose new room
        new_room = switch_dict.get(input_text)

        # Default value of any x_to attribute is None. Check if this is a valid direction.
        if new_room != None:
            # Set new room and print location
            self.current_room = new_room
            self.get_current_room()
            return
        else:
            print("Can't go that way. Valid inputs are: (n)orth, (s)outh, (e)ast, (w)est, look, inv, take (item), drop (item)\n")
            return

    ##################################################

    def set_inventory_item(self, item):
        for i in self.current_room.items:
            if i.name.lower() == item.lower():
                self.inventory.append(i)
                self.current_room.remove_item(i)
                print("You have picked up a " + i.name + "\n")
                return
        return

    def drop_inventory_item(self, item):
        if len(self.inventory) != 0:
            for i in self.inventory:
                if i.name.lower() == item.lower():
                    self.current_room.set_item(i)
                    self.inventory.remove(i)
                    print("You have dropped a " + i.name + "\n")
                    return
        return

    def get_inventory(self):
        if len(self.inventory) >= 1:
            print("Currently holding:\n")
            for item in self.inventory:
                print(item.name + "")
                print(item.description + "\n")
            return
        else:
            print("Currently holding: Nothing\n")
            return

    ##################################################