import arcade
from pathlib import Path

from src.entities.stats import CharacterStats

ENTITY_SCALING_FACTOR = 0.1
ANIMATION_SPEED = 0.05

class Entity(arcade.Sprite):
    def __init__(
            self,
            init_position: tuple[int,int],
            running_assets_folder: Path,
            idle_assets_folder: Path,
        ):

        super().__init__(
            scale=ENTITY_SCALING_FACTOR,
            center_x=init_position[0],
            center_y=init_position[1]
        )

        self.stats = CharacterStats(
            max_health=100,
            health=100,
            speed=200,
            damage=10
        )

        self.running_textures = self._load_animation(running_assets_folder)
        self.idle_textures = self._load_animation(idle_assets_folder)

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


    @property
    def speed(self) -> float:
        return self.stats.speed

    @property
    def health(self) -> int:
        return self.stats.health


    @property
    def max_health(self) -> int:
        return self.stats.max_health


    @property
    def xp(self) -> int:
        return self.stats.xp

    @property
    def level(self):
        return self.stats.level