import arcade
import os

from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent.parent
SPRITE_PATH = CURRENT_DIR.parent / "assets" / "sprites"


class Slash(arcade.Sprite):
    def __init__(
        self,
        position: tuple[float, float],
        facing: tuple[float, float],
        cooldown: float,
    ):
        super().__init__()
        self.frames = []
        self.current_frame = 0
        self.animation_timer = 0.0

        # Load textures
        texture_folder = SPRITE_PATH / "weapons/slash"

        textures = sorted(texture_folder.glob("*.png"))
        self.frames = [arcade.load_texture(str(f)) for f in textures]

        self.animation_speed = cooldown / (len(self.frames) * 2)

        self.texture = self.frames[0]
        self.center_x, self.center_y = position

        # Optionally rotate sprite based on facing
        self.angle = self._facing_to_angle(facing)

    def _facing_to_angle(self, facing):
        import math

        dx, dy = facing
        return math.degrees(math.atan2(dy, dx))

    def update_animation(self, delta_time: float = 1 / 60):
        self.animation_timer += delta_time
        if self.animation_timer > self.animation_speed:
            self.animation_timer = 0
            self.current_frame += 1
            if self.current_frame < len(self.frames):
                self.texture = self.frames[self.current_frame]
            else:
                self.kill()
