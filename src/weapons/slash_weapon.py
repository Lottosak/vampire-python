import math
from src.weapons.weapon import Weapon
import arcade
from src.weapons.slash import Slash


class SlashWeapon(Weapon):
    def __init__(self, owner, damage=100, cooldown=1.0, range=60, arc_width=90):
        super().__init__(owner, damage, cooldown)
        self.range = range
        self.arc_width = arc_width  # in degrees
        self.slash_list = arcade.SpriteList()

    def attack(self, enemies: arcade.SpriteList):
        slash = Slash(self.owner.position, self.owner.facing_direction, self.cooldown)
        self.slash_list.append(slash)

        for enemy in enemies:
            dx = enemy.center_x - self.owner.center_x
            dy = enemy.center_y - self.owner.center_y
            distance = math.hypot(dx, dy)

            if distance <= self.range:
                angle_to_enemy = math.degrees(math.atan2(dy, dx))
                facing_angle = math.degrees(
                    math.atan2(
                        self.owner.facing_direction[1],
                        self.owner.facing_direction[0],
                    )
                )

                delta_angle = (angle_to_enemy - facing_angle + 360) % 360
                if delta_angle > 180:
                    delta_angle -= 360

                if abs(delta_angle) <= self.arc_width / 2:
                    enemy.take_damage(self.damage)

    def draw(self):
        self.slash_list.draw()

    def update_animation(self, delta_time: float):
        self.slash_list.update_animation(delta_time)
