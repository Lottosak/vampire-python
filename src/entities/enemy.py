from pathlib import Path

from src.entities.entity import Entity

CURRENT_DIR = Path(__file__).resolve().parent.parent
SPRITE_PATH = CURRENT_DIR.parent / "assets" / "sprites"

class Enemy(Entity):
    def __init__(self,
                 init_position: tuple[int, int],
                 running_folder: Path,
                 idle_folder: Path):
        super().__init__(
            init_position=init_position,
            running_assets_folder=running_folder,
            idle_assets_folder=idle_folder
        )



