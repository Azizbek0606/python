from abc import ABC, abstractmethod
import random


class Weapon(ABC):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    @abstractmethod
    def attack(self, target):
        pass


class MeleeWeapon(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

    def attack(self, target):
        pass

class Sword(MeleeWeapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

    def attack(self, target):
        target.take_damage(self.damage)


class Axe(MeleeWeapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

    def attack(self, target):
        target.take_damage(self.damage)


class RangedWeapon(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

    def attack(self, target):
        pass

class Bow(MeleeWeapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

    def attack(self, target):
        target.take_damage(self.damage)

class Crossbow(MeleeWeapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

    def attack(self, target):
        target.take_damage(self.damage)


class Character(ABC):
    def __init__(self, name, health, defense):
        self.name = name
        self.health = health
        self.defense = defense
    @abstractmethod
    def attack(self):
        pass
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def take_damage(self, damage):
        pass



class Enemy(Character):
    def __init__(self, name, health, defense, damage):
        super().__init__(name, health, defense)
        self.damage = damage

    def attack(self, target: Character):
        pass

    def take_damage(self, damage):
        pass

    def info(self):
        pass


class Player(Character):
    def __init__(self, name, health, defense, weapon):
        super().__init__(name, health, defense)
        self.weapon = weapon

    def info(self):
        return f'\nname:{self.name},  health:{self.health},  defense:{self.defense},  Weapon: {self.weapon.name}'

    def attack(self, target: Character):
        self.weapon.attack(target)

    def take_damage(self, damage):
        self.health -= damage



class Wolf(Character):
    def __init__(self, name, health, defense, damage):
        super().__init__(name, health, defense)
        self.damage = damage

    def attack(self, target: Character):
        target.take_damage(self.damage)

    def take_damage(self, damage):
        self.health -= damage

    def info(self):
        return f"name: {self.name}, health: {self.health}, defense: {self.defense}, damage: {self.damage}"


class Lion(Character):
    def __init__(self, name, health, defense, damage):
        super().__init__(name, health, defense)
        self.damage = damage

    def attack(self, target: Character):
        target.take_damage(self.damage)

    def take_damage(self, damage):
        self.health -= damage

    def info(self):
        return f"name: {self.name}, health: {self.health}, defense: {self.defense}, damage: {self.damage}"

class Tiger(Character):
    def __init__(self, name, health, defense, damage):
        super().__init__(name, health, defense)
        self.damage = damage

    def attack(self, target: Character):
        target.take_damage(self.damage)

    def take_damage(self, damage):
        self.health -= damage

    def info(self):
        return f"name: {self.name}, health: {self.health}, defense: {self.defense}, damage: {self.damage}"


sword = Sword('sword', 15)
axe = Axe('axe', 13)
bow = Bow('bow', 12)
crossbow = Crossbow('crossbow', 17)


wolf = Wolf('wolf', 50, 20, 12)
lion = Lion('lion', 70, 20, 12)
tiger = Tiger('tiger', 90, 20, 15)

weapons = [sword, axe, bow, crossbow]
enemy = [wolf, lion, tiger]

def game(weapon, enemy):

    print("choose weapon: ")
    for i in range(len(weapon)):
        print(i+ 1 , "--", weapon[i].name)
    x = int(input(f"Enter nuber from 1 to {len(weapon)}: ")) - 1
    player = Player("Bob", 100, 50, weapon[x])
    is_continue = player.health > 0
    raunds = 0

    while is_continue:
        target = get_enemy(enemy)
        raunds += 1
        while is_continue:
            if target.health > 0:
                player.attack(target)
                print(player.info())
                target.attack(player)
                print(target.info())
            else:
                bonus_hp = random.randint(player.health, 100)
                player.health += bonus_hp
                print(f"{raunds} - raund ended, player takes {bonus_hp} hp")
                break

def get_enemy(enemy):
    return enemy[random.randint(0, (len(enemy) - 1))]

game(weapons,enemy)