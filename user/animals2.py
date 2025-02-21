# Создаём базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# Реализуем наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`

class Animal():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} ест.")


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return "Чирик!"

class Mammal(Animal):
    def __init__(self, name, age, habitat):
         super().__init__(name, age)
         self.habitat = habitat

    def make_sound(self):
        return "Рррр!"

class Reptile(Animal):

     def __init__(self, name, age, scale_type):
         super().__init__(name, age)
         self.scale_type = scale_type

     def make_sound(self):
         return "Шшш!"

     def animal_sound(animals):
      for animal in animals:
        print(f"{animal.name} говорит: {animal.make_sound()}")

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")


class Zoo:
     def __init__(self):
        self.animals = []
        self.staff = []

     def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк.")

     def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Сотрудник {staff_member.name} добавлен в зоопарк.")

if __name__ == "__main__":

    parrot = Bird(name="Попугай", age=4, wing_span=15)
    lion = Mammal(name="Лев", age=5, habitat="Савана")
    snake = Reptile(name="Змея", age=3, scale_type="Чешуя")

    zoo = Zoo()
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)

    zookeeper = ZooKeeper(name="Александр")
    veterinarian = Veterinarian(name="Николай")

    zoo.add_staff(zookeeper)
    zoo.add_staff(veterinarian)

    animal_sound = zoo.animals

    zookeeper.feed_animal(lion)
    veterinarian.heal_animal(snake)








