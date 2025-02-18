# Создание класса Store, который можно будет использовать для создания различных магазинов.

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден.")


# Создание объектов класса
store1 = Store("Магазин №59", "Улица Машиностроителей")
store2 = Store("Магазин №130", "Улица Белореченская")
store3 = Store("Магазин 65", "Улица Ильича")

# Добавление товаров в магазины
store1.add_item("Яблоки", 50)
store1.add_item("Бананы", 75)
store2.add_item("Хлеб", 69)
store2.add_item("Кефир", 59)
store3.add_item("Кофе", 249)
store3.add_item("Чай", 140)

# Тестирование методов магазина
print("\nТестирование магазина №59:")
store1.add_item("Груши", 70)
print("Цена яблок:", store1.get_price("Яблоки"))
store1.update_price("Бананы", 80)
store1.remove_item("Яблоки")
print("Цена яблок после удаления:", store1.get_price("Яблоки"))



