import arcade

# Constants for screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Vampire Survivors Clone"

class VampireGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

    def setup(self):
        """Initial setup of the game"""
        pass

    def on_draw(self):
        """Render the screen"""
        arcade.start_render()
        arcade.draw_text("Game Loop Running...", 250, 300,
                         arcade.color.WHITE, 20, font_name="Arial")

    def on_update(self, delta_time):
        pass
