class Item:
    def __init__(self, name, price, quantity):
        self.item_name = name
        self.price = price
        self.quantity =  quantity
      
    def __repr__ (self):
      return (f"Item Name: {self.item_name}, Price: {self.price}, Quantity: {self.quantity}")

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = []

    def add_item(self, name):
      self.inventory.append(name)

    def display_contents(self):
      return f"{self.inventory}"

Item1 = Item("Chuckie", 30, 100)
Sari_Sari_store = Store("Sari-sari Store")
Sari_Sari_store.add_item(Item1)
print(Sari_Sari_store.display_contents())
print("ILABYUMARIE")
print("MArie will pass")
