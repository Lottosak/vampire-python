from pathlib import Path
import math

from src.entities.entity import Entity
from src.entities.player import Player

CURRENT_DIR = Path(__file__).resolve().parent.parent
SPRITE_PATH = CURRENT_DIR.parent / "assets" / "sprites"


class Enemy(Entity):
    def __init__(
        self,
        init_position: tuple[int, int],
        running_folder: Path,
        idle_folder: Path,
        player: Player,
    ):
        super().__init__(
            init_position=init_position,
            running_assets_folder=running_folder,
            idle_assets_folder=idle_folder,
        )
        self.player = player

    def follow_player(self, delta_time: float) -> None:
        dx = self.player.center_x - self.center_x
        dy = self.player.center_y - self.center_y
        distance = math.hypot(dx, dy)

        if distance > 0:
            dx /= distance
            dy /= distance
            self.center_x += dx * self.speed * 1 / 60
            self.center_y += dy * self.speed * 1 / 60

        self.set_direction(dx)
        self.set_movement_state(dx != 0 or dy != 0)

        self.update_animation(delta_time)
