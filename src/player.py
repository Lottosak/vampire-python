import arcade
from pathlib import Path

PLAYER_SCALING = 0.1
CURRENT_DIR = Path(__file__).resolve().parent
SPRITE_PATH = CURRENT_DIR.parent / "assets" / "sprites"
ANIMATION_SPEED = 0.05


class Player(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__(
            scale=PLAYER_SCALING,
            center_x=center_x,
            center_y=center_y
        )

        running_folder = SPRITE_PATH / "player" / "running"
        idle_folder = SPRITE_PATH / "player" / "idle"

        self.running_textures = self._load_animation(running_folder)
        self.idle_textures = self._load_animation(idle_folder)

        self.facing = "right"
        self.current_textures = self.idle_textures[self.facing]
        self.current_frame_index = 0
        self.time_since_last_frame = 0
        self.texture = self.current_textures[0]

        self.is_moving = False

    def _load_animation(self, folder):
        frames = sorted(folder.glob(f"*.png"))
        original = [arcade.load_texture(str(f)) for f in frames]
        flipped = [arcade.load_texture(str(f), mirrored=True) for f in frames]
        return {"right": original, "left": flipped}

    def set_movement_state(self, is_moving: bool):
        if self.is_moving != is_moving:
            self.is_moving = is_moving
            base_textures = self.running_textures if is_moving else self.idle_textures
            self.current_textures = base_textures[self.facing]
            self.current_frame_index = 0
            self.time_since_last_frame = 0
            self.texture = self.current_textures[0]

    def update_animation(self, delta_time: float = 1 / 60):
        self.time_since_last_frame += delta_time

        if self.time_since_last_frame > ANIMATION_SPEED:
            self.current_frame_index = (self.current_frame_index + 1) % len(self.current_textures)
            self.texture = self.current_textures[self.current_frame_index]
            self.time_since_last_frame = 0

    def set_direction(self, dx: float):
        if dx > 0:
            new_facing = "right"
        elif dx < 0:
            new_facing = "left"
        else:
            return  # no change

        if new_facing != self.facing:
            self.facing = new_facing
            base_textures = self.running_textures if self.is_moving else self.idle_textures
            self.current_textures = base_textures[self.facing]
            self.current_frame_index = 0
            self.texture = self.current_textures[0]

    def getSpeed(self) -> float:
        return 200.0

