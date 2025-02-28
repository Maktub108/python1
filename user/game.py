# Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.|

from abc import ABC, abstractmethod
import random

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука."

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack_monster(self, monster):
        if self.weapon:
            print(self.weapon.attack())
            damage = random.randint(1, 15)  # Симуляция урона
            monster.take_damage(damage)
            if monster.is_defeated():
                print("Монстр побежден!")
            else:
                print(f"Монстр остался в живых с {monster.health} здоровья.")
        else:
            print("У бойца нет оружия!")

class Monster:
    def __init__(self, health):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage

    def is_defeated(self):
        return self.health <= 0


def main():

    fighter = Fighter("Воин")
    monster = Monster(30)

    fighter.change_weapon(Sword())
    print(f"{fighter.name} выбирает меч.")
    fighter.attack_monster(monster)

    fighter.change_weapon(Bow())
    print(f"{fighter.name} выбирает лук.")
    fighter.attack_monster(monster)

if __name__ == "__main__":
    main()
