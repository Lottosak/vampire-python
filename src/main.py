import arcade

from game import VampireGame

def main():
    game = VampireGame()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
