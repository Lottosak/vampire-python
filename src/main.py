import arcade

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Test Game")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Hello Arcade!", 300, 300, arcade.color.WHITE, 18)

if __name__ == "__main__":
    game = MyGame()
    arcade.run()
