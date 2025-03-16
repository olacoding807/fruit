

# List of fruits
items = ["Apple", "Banana"]

# Function to add a new fruit
def add_item(new_item):
    global items
    items.append(new_item)
    print(f"Updated list: {items}")

# Adding fruits
add_item("Orange")
add_item("Grapes")
add_item("Cherries")
add_item("Strawberries")

# Fruit class (replacing Car class)
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display_info(self):
        # Example use of fruit details
        print(f"Fruit Name: {self.name}, Color: {self.color}")

# Example of creating and displaying a fruit
fruit_example = Fruit("Mango", "Yellow")
fruit_example.display_info()
