import random
import math
from pathlib import Path

from src.entities.enemy import Enemy

MIN_SPAWN_DISTANCE = 150

CURRENT_DIR = Path(__file__).resolve().parent
SPRITE_PATH = CURRENT_DIR.parent / "assets" / "sprites"

class Spawner:
    def __init__(self, arena_size: tuple[int, int]):
        self.arena_size = arena_size

    def get_spawn_position_around_player(self, player_position: tuple[int, int]) -> tuple[int, int]:
        while True:
            x = int(random.uniform(0, self.arena_size[0]))
            y = int(random.uniform(0, self.arena_size[1]))

            dx = x - player_position[0]
            dy = y - player_position[1]
            distance = math.hypot(dx, dy)

            if distance >= MIN_SPAWN_DISTANCE:
                return x, y

    def spawn_enemy(self, player_position: tuple[int, int]) -> Enemy:
        spawn_position = self.get_spawn_position_around_player(player_position)

        #TODO: for now spawn same sprites as player, later choose what enemy to spawn
        enemy_running_textures = SPRITE_PATH / "player" / "running"
        enemy_idle_textures = SPRITE_PATH / "player" / "idle"

        return Enemy(
            init_position=spawn_position,
            running_folder=enemy_running_textures,
            idle_folder=enemy_idle_textures
        )