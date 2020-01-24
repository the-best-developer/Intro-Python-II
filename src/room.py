# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def get_room_items(self):
        if len(self.items) != 0:
            for item in self.items:
                print(item.name + " Found!")
                print(item.description + "\n")
            return
        else:
            print("No items found.\n")
            return

    def set_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)