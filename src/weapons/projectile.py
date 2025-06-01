import arcade


class Projectile(arcade.Sprite):
    def __init__(self, position, direction, damage, speed=400):
        super().__init__("assets/projectile.png", scale=0.5)
        self.center_x, self.center_y = position
        self.change_x = direction[0] * speed
        self.change_y = direction[1] * speed
        self.damage = damage

    def update(self):
        self.center_x += self.change_x * 1 / 60
        self.center_y += self.change_y * 1 / 60
