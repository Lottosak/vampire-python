from dataclasses import dataclass


@dataclass
class CharacterStats:
    max_health: int
    health: int
    speed: float
    damage: int
    level: int = 1
    xp: int = 0
    invulnerable: bool = False
    invulnerable_time: float = 0

    def take_damage(self, amount: int):
        if not self.invulnerable:
            self.health -= amount
            self.invulnerable = True
            self.invulnerable_time = 1.0  # seconds of i-frames
            print(f"Character took {amount} damage. HP: {self.health}/{self.max_health}")
            return self.health <= 0
        return False

    def gain_xp(self, amount: int):
        self.xp += amount
        xp_to_level = 100 + (self.level - 1) * 20
        if self.xp >= xp_to_level:
            self.xp -= xp_to_level
            self.level += 1
            self.max_health += 10
            self.health = self.max_health
            print(f"Leveled up to {self.level}!")
