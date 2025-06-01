import math
import random
from pathlib import Path

from src.entities.enemy import Enemy
from src.entities.player import Player

MIN_SPAWN_DISTANCE = 150

CURRENT_DIR = Path(__file__).resolve().parent
SPRITE_PATH = CURRENT_DIR.parent / "assets" / "sprites"


class Spawner:
    def __init__(self, arena_size: tuple[int, int], player: Player):
        self.arena_size = arena_size
        self.player = player

    def get_spawn_position_around_player(
        self,
    ) -> tuple[int, int]:
        while True:
            x = int(random.uniform(0, self.arena_size[0]))
            y = int(random.uniform(0, self.arena_size[1]))

            dx = x - self.player.center_x
            dy = y - self.player.center_y
            distance = math.hypot(dx, dy)

            if distance >= MIN_SPAWN_DISTANCE:
                return x, y

    def spawn_enemy(self) -> Enemy:
        spawn_position = self.get_spawn_position_around_player()

        # TODO: for now spawn same sprites as player, later choose what enemy to spawn
        enemy_running_textures = SPRITE_PATH / "skeleton" / "running"
        enemy_idle_textures = SPRITE_PATH / "skeleton" / "idle"

        return Enemy(
            init_position=spawn_position,
            running_folder=enemy_running_textures,
            idle_folder=enemy_idle_textures,
            player=self.player,
        )
