
# OOP 

# 1. Abstraction 
# 2. Encapsulation
# 3. Inheritance
# 4. Polymorphism

# Class -> Object/Instances - blueprint
# attributes - make up the individual instance
# - hair color
# - height
# - name
# - energy

# methods - action that an instance can take
# - walk
# - throw
# - sleep


def add(num1, num2):
    return num1 + num2

# function -> methods

import random


class Weapons:
    pass

class Person:
    
    def __init__(self, name, height, hair_color, energy=100, health=100):
        self.name = name
        self.height = height
        self.hair_color = hair_color
        self.energy = energy
        self.health = health
        self.is_alive = True

    def __repr__(self):
        return f"{self.name} | {self.health}"

    def say_name(self):
        print(f"My name is {self.name}")
        return self

    def what_is_hair_color(self):
        print(f"My hair color is {self.hair_color}")
        return self
    
    def change_health(self, amount):
        self.health += amount
        print(f"you changed health by {amount}")
        if self.health <= 0:
            self.is_alive = False
        return self

    def punch(self, victim):
        damage = random.randint(1,10) 
        print(f"{self.name} is going to do {damage} damage to {victim.name}")
        
        # This is bad practice
        victim.change_health(-damage)
        
        return self
    
    def stats(self):
        # attributes = dictionary
        attributes = self.__dict__
        for key in attributes:
            val = attributes[key]
            print(f"{key}: {val}")

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.current_turn = None
        self.not_current_turn = None
        self.winner = None
        self.is_playing = False

    def choose_starting_player(self):
        starting_turn_num = random.randint(0,100)
        starting_turn_mod = starting_turn_num % 2

        if starting_turn_mod == 0:
            self.current_turn = p1
            self.not_current_turn = p2
        else: 
            self.current_turn = p2
            self.not_current_turn = p1

    def switch_turns(self):
        # switch turns
        temp = self.current_turn
        self.current_turn = self.not_current_turn
        self.not_current_turn = temp
        return self

    def show_stat(self):
        print("-"*40)
        self.p1.stats()
        print("="*40)
        self.p2.stats()
        print("-"*40)

    def battle(self):
        self.is_playing = True
        self.choose_starting_player()

        while p1.is_alive and p2.is_alive:
            self.current_turn.punch(self.not_current_turn)
            self.switch_turns()

p1 = Person("Chris", 6.4, "red")
p2 = Person("Tyler", 5.8, None, 85)
g1 = Game(p1, p2)
g1.battle()


