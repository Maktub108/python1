class Store():

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"товар {item_name} был добавлен в {self.name}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"товар {item_name} удален из {self.name}")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"цена на товар {item_name} обновлена в {self.name}")
        else:
            print(f"товар {item_name} не найден")
store1 = Store("Монетка", "Кузнецова 2")
store2 = Store("Кировский", "Машиностроителей 62")
store3 = Store("Верный", "Бардина 25")

store1.add_item("сахар", 79)
store1.add_item("молоко", 110)
store1.add_item("кефир", 59)

store1.remove_item("сахар")
print(store1.get_price("молоко"))

store1.update_price("кефир", 70)




