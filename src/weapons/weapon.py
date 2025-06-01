from abc import ABC, abstractmethod

import arcade


class Weapon(ABC):
    def __init__(self, owner, damage: int, cooldown: float):
        self.owner = owner
        self.damage = damage
        self.cooldown = cooldown
        self.timer = 0.0

    def update(self, delta_time: float, enemies: arcade.SpriteList):
        self.timer += delta_time
        self.update_animation(delta_time)
        if self.timer >= self.cooldown:
            self.attack(enemies)
            self.timer = 0.0

    @abstractmethod
    def attack(self, enemies: arcade.SpriteList):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def update_animation(self, delta_time: float):
        pass
