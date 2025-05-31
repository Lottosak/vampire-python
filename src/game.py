import arcade

from player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Vampire Survivors Clone"

class VampireGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

        self.player = None
        self.keys = set()

    def setup(self):
        """Initial setup of the game"""
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def on_draw(self):
        """Render the screen"""
        arcade.start_render()
        self.player.draw()
        self.draw_hud()

    def draw_hud(self):
        arcade.draw_text(f"HP: {self.player.health}/{self.player.max_health}", 10, self.height - 20,
                         arcade.color.WHITE, 14)
        arcade.draw_text(f"Level: {self.player.level}", 10, self.height - 40, arcade.color.WHITE, 14)
        arcade.draw_text(f"XP: {self.player.xp}", 10, self.height - 60, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        dx = 0
        dy = 0
        if arcade.key.W in self.keys:
            dy += self.player.speed * delta_time
        if arcade.key.S in self.keys:
            dy -= self.player.speed * delta_time
        if arcade.key.A in self.keys:
            dx -= self.player.speed * delta_time
        if arcade.key.D in self.keys:
            dx += self.player.speed * delta_time

        self.player.center_x += dx
        self.player.center_y += dy

        self.player.set_direction(dx)
        self.player.set_movement_state(dx != 0 or dy != 0)

        self.player.update_animation(delta_time)

    def on_key_press(self, key, modifiers):
        self.keys.add(key)

    def on_key_release(self, key, modifiers):
        self.keys.discard(key)