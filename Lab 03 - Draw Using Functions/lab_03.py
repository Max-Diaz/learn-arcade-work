"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

# Ground
arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

# Cybertruck
arcade.draw_rectangle_filled(160, 60, 210, 50, arcade.color.BATTLESHIP_GREY)
arcade.draw_triangle_filled(20, 35, 100, 35, 50, 90, arcade.color.BATTLESHIP_GREY)
arcade.draw_triangle_filled(295, 85, 250, 85, 265, 33, arcade.color.BATTLESHIP_GREY)
arcade.draw_triangle_filled(42, 85, 150, 85, 150, 120, arcade.color.BLIZZARD_BLUE)
arcade.draw_triangle_filled(150, 85, 150, 120, 300, 85, arcade.color.BLIZZARD_BLUE)
arcade.draw_circle_filled(80, 40, 30, arcade.csscolor.BLACK)
arcade.draw_circle_filled(230, 40, 30, arcade.csscolor.BLACK)
arcade.draw_circle_filled(80, 40, 20, arcade.csscolor.DARK_SLATE_GREY)
arcade.draw_circle_filled(230, 40, 20, arcade.csscolor.DARK_SLATE_GREY)
arcade.draw_circle_filled(280, 75, 7, arcade.csscolor.YELLOW)




# Finish and run
arcade.finish_render()
arcade.run()
