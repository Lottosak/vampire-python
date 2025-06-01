from weapon import Weapon
from projectile import Projectile


class ProjectileWeapon(Weapon):
    def attack(self, target_list, projectile_list):
        projectile = Projectile(
            position=(self.owner.center_x, self.owner.center_y),
            direction=self.owner.facing_direction,  # assume vector (x, y)
            damage=self.damage,
        )
        projectile_list.append(projectile)
