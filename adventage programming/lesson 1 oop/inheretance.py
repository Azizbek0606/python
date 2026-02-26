from abc import ABC, abstractmethod
import random

# Abstract BaseWeapon interface
class BaseWeapon(ABC):
    @abstractmethod
    def get_damage(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

# Melee weapons
class Sword(BaseWeapon):
    def get_damage(self):
        return random.randint(10, 20)  # High damage, close range

    def get_name(self):
        return "Sword"

class Hammer(BaseWeapon):
    def get_damage(self):
        return random.randint(15, 25)  # Higher damage but maybe slower, but for simplicity same

    def get_name(self):
        return "Hammer"

# Ranged weapons
class Bow(BaseWeapon):
    def get_damage(self):
        return random.randint(8, 15)  # Medium damage

    def get_name(self):
        return "Bow"

class Crossbow(BaseWeapon):
    def get_damage(self):
        return random.randint(12, 18)  # Slightly higher

    def get_name(self):
        return "Crossbow"

# Magic weapons
class Fire(BaseWeapon):
    def get_damage(self):
        return random.randint(15, 30)  # High variance

    def get_name(self):
        return "Fire Magic"

class Ice(BaseWeapon):
    def get_damage(self):
        return random.randint(10, 25)  # Freeze effect, but for simplicity damage only

    def get_name(self):
        return "Ice Magic"

# Abstract BaseCharacter interface
class BaseCharacter(ABC):
    def __init__(self, hp):
        self.hp = hp

    @abstractmethod
    def attack(self, enemy):
        pass

    def is_alive(self):
        return self.hp > 0

# Player class
class Player(BaseCharacter):
    def __init__(self, weapon):
        super().__init__(100)  # Default HP 100
        self.weapon = weapon

    def attack(self, enemy):
        damage = self.weapon.get_damage()
        enemy.hp -= damage
        print(f"Player attacks with {self.weapon.get_name()} for {damage} damage. Enemy HP: {enemy.hp if enemy.hp > 0 else 0}")

# Enemy subclasses
class Enemy(BaseCharacter):
    @abstractmethod
    def get_name(self):
        pass

class Goblin(Enemy):
    def __init__(self):
        super().__init__(50)  # Low HP
        self.damage = random.randint(10, 15)  # Medium damage

    def attack(self, player):
        player.hp -= self.damage
        print(f"Goblin attacks for {self.damage} damage. Player HP: {player.hp if player.hp > 0 else 0}")

    def get_name(self):
        return "Goblin"

class Orc(Enemy):
    def __init__(self):
        super().__init__(150)  # High HP
        self.damage = random.randint(5, 10)  # Low damage

    def attack(self, player):
        player.hp -= self.damage
        print(f"Orc attacks for {self.damage} damage. Player HP: {player.hp if player.hp > 0 else 0}")

    def get_name(self):
        return "Orc"

class Troll(Enemy):  # Added a third enemy for completeness: Medium HP, high damage, slow
    def __init__(self):
        super().__init__(100)  # Medium HP
        self.damage = random.randint(15, 20)  # High damage

    def attack(self, player):
        player.hp -= self.damage
        print(f"Troll attacks for {self.damage} damage. Player HP: {player.hp if player.hp > 0 else 0}")

    def get_name(self):
        return "Troll"

# Game logic
def choose_weapon():
    print("Choose your weapon:")
    print("1. Sword (Melee)")
    print("2. Hammer (Melee)")
    print("3. Bow (Ranged)")
    print("4. Crossbow (Ranged)")
    print("5. Fire (Magic)")
    print("6. Ice (Magic)")
    choice = int(input("Enter number: "))
    weapons = [Sword(), Hammer(), Bow(), Crossbow(), Fire(), Ice()]
    return weapons[choice - 1]

def get_random_enemy():
    enemies = [Goblin(), Orc(), Troll()]
    return random.choice(enemies)

def fight(player, enemy):
    print(f"\nFighting {enemy.get_name()} (HP: {enemy.hp})")
    while player.is_alive() and enemy.is_alive():
        player.attack(enemy)
        if enemy.is_alive():
            enemy.attack(player)
    return player.is_alive()

def main():
    weapon = choose_weapon()
    player = Player(weapon)
    score = 0
    round_num = 1

    while player.is_alive():
        enemy = get_random_enemy()
        if fight(player, enemy):
            score += 1
            player.hp += 20  # Add HP after each win for better gameplay
            player.hp = min(player.hp, 200)  # Cap at 200
            print(f"Round {round_num} won! Score: {score}. Player HP restored to {player.hp}")
            round_num += 1
        else:
            print(f"Game over! Total score: {score}")
            break

if __name__ == "__main__":
    main()