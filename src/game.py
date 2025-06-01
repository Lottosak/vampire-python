import arcade

from src.entities.player import Player
from src.entities.enemy import Enemy
from src.spawner import Spawner

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Vampire Survivors Clone"


class VampireGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

        self.spawner = None
        self.player = None
        self.enemy_spawn_timer = 0.0
        self.enemy_spawn_interval = 1.5
        self.enemy_list: arcade.SpriteList[Enemy] = arcade.SpriteList()

    def setup(self) -> None:
        """Initial setup of the game"""
        self.player = Player((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.spawner = Spawner((SCREEN_WIDTH, SCREEN_HEIGHT), self.player)

    def on_draw(self) -> None:
        """Render the screen"""
        arcade.start_render()
        self.player.draw()
        self.enemy_list.draw()
        self.draw_hud()
        for weapon in self.player.get_weapons():
            weapon.draw()

    def draw_hud(self) -> None:
        arcade.draw_text(
            f"HP: {self.player.health}/{self.player.max_health}",
            10,
            self.height - 20,
            arcade.color.WHITE,
            14,
        )
        arcade.draw_text(
            f"Level: {self.player.level}", 10, self.height - 40, arcade.color.WHITE, 14
        )
        arcade.draw_text(
            f"XP: {self.player.xp}", 10, self.height - 60, arcade.color.WHITE, 14
        )

    def on_update(self, delta_time: float):
        self.player.update_position(delta_time)
        for weapon in self.player.get_weapons():
            weapon.update(delta_time, self.enemy_list)

        self.enemy_spawn_timer += delta_time
        if self.enemy_spawn_timer > self.enemy_spawn_interval:
            self.enemy_spawn_timer = 0
            self.enemy_list.append(self.spawner.spawn_enemy())

        for enemy in self.enemy_list:
            enemy.follow_player(delta_time)

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        self.player.on_key_press(symbol)

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self.player.on_key_release(symbol)
