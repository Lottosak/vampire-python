from pathlib import Path

import arcade

from src.entities.entity import Entity

CURRENT_DIR = Path(__file__).resolve().parent.parent
SPRITE_PATH = CURRENT_DIR.parent / "assets" / "sprites"


class Player(Entity):
    def __init__(self, init_position: tuple[int, int]):
        super().__init__(
            init_position=init_position,
            running_assets_folder=SPRITE_PATH / "player" / "running",
            idle_assets_folder=SPRITE_PATH / "player" / "idle",
        )

        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

    def update_position(self, delta_time: float) -> None:
        dx = 0
        dy = 0
        if self.move_up:
            dy += self.speed * delta_time
        if self.move_down:
            dy -= self.speed * delta_time
        if self.move_left:
            dx -= self.speed * delta_time
        if self.move_right:
            dx += self.speed * delta_time

        self.center_x += dx
        self.center_y += dy

        self.set_direction(dx)
        self.set_movement_state(dx != 0 or dy != 0)

        self.update_animation(delta_time)

    def on_key_press(self, key: int) -> None:
        if key == arcade.key.W:
            self.move_up = True
        if key == arcade.key.S:
            self.move_down = True
        if key == arcade.key.A:
            self.move_left = True
        if key == arcade.key.D:
            self.move_right = True

    def on_key_release(self, key: int) -> None:
        if key == arcade.key.W:
            self.move_up = False
        if key == arcade.key.S:
            self.move_down = False
        if key == arcade.key.A:
            self.move_left = False
        if key == arcade.key.D:
            self.move_right = False
