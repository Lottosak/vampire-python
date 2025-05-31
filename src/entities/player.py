from pathlib import Path

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
