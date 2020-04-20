# **********************************  Set builder program  ******************************************

# Imports
import arcade
import app
import os
import sys

# globals used to set dimensions of game window
SCREENWIDTH = 950
SCREENHEIGHT = 600
SCREENTITLE = "Set Builder"
"""username = input(str("Welcome to the set builder game! Enter your name to get started: "))
print("welcome",username)"""

# os.system("python3 -m flask run") >>>>>>>>>>>>>>>>>>>>> UNCOMMENT FOR FLASK WEB APP IMPLEMENTATION

class setBuilder(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)
        self.text_angle = 0
        self.time_elapsed = 0.0

    def on_update(self, delta_time):
        self.text_angle += 1
        self.time_elapsed += delta_time

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # start_x and start_y make the start point for the text. We draw a dot to make it easy too see
        # the text in relation to its start x and y.
        start_x = 280
        start_y = 500
        arcade.draw_text("Welcome to the set builder game!", start_x, start_y, arcade.color.RED, 21)

def main():
    setBuilder(SCREENWIDTH, SCREENHEIGHT, SCREENTITLE)
    arcade.run()


if __name__ == "__main__":
    main()