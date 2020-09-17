"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(800, 600, "Drawing Example")

# Set the background
arcade.set_background_color(arcade.color.SAE)

# Get ready to draw
arcade.start_render()

# Ground
arcade.draw_lrtb_rectangle_filled(0, 799, 200, 0, arcade.color.ALLOY_ORANGE)

# Buildings
arcade.draw_rectangle_filled(100, 350, 100, 300, arcade.color.BATTLESHIP_GREY)
arcade.draw_rectangle_filled(300, 300, 200, 200, arcade.color.BATTLESHIP_GREY)
arcade.draw_rectangle_filled(475, 350, 100, 300, arcade.color.BATTLESHIP_GREY)
arcade.draw_rectangle_filled(650, 300, 200, 200, arcade.color.BATTLESHIP_GREY)

# Windows
arcade.draw_rectangle_filled(100, 350, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(100, 450, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(100, 250, 30, 30, arcade.color.BABY_BLUE)

# Windows
arcade.draw_rectangle_filled(250, 350, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(250, 250, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(300, 250, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(300, 250, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(300, 350, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(350, 250, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(350, 350, 30, 30, arcade.color.BABY_BLUE)


# Windows
arcade.draw_rectangle_filled(475, 350, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(475, 300, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(475, 400, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(475, 450, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(475, 250, 30, 30, arcade.color.BABY_BLUE)

# Windows
arcade.draw_rectangle_filled(585, 375, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(585, 325, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(585, 275, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(655, 375, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(655, 325, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(655, 275, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(720, 375, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(720, 325, 30, 30, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(720, 275, 30, 30, arcade.color.BABY_BLUE)

# Further Undefined Bulidings in the Background
arcade.draw_rectangle_filled(175, 340, 50, 280, arcade.color.BLACK)
arcade.draw_rectangle_filled(355, 440, 150, 90, arcade.color.BLACK)
arcade.draw_rectangle_filled(410, 341, 40, 290, arcade.color.BLACK)
arcade.draw_rectangle_filled(513, 520, 80, 40, arcade.color.BLACK)
arcade.draw_rectangle_filled(535, 350, 35, 305, arcade.color.BLACK)
arcade.draw_rectangle_filled(680, 428, 140, 60, arcade.color.BLACK)
arcade.draw_rectangle_filled(775, 350, 50, 305, arcade.color.BLACK)
arcade.draw_rectangle_filled(20, 310, 60, 220, arcade.color.BLACK)

# Doomer Guy
arcade.draw_rectangle_filled(350, 100, 10,  35, arcade.color.BLACK)
arcade.draw_circle_filled(350, 120, 10, arcade.color.BLACK)
arcade.draw_triangle_filled(344, 110, 346, 100, 335, 75, arcade.color.BLACK)
arcade.draw_triangle_filled(355, 110, 355, 100, 373, 75, arcade.color.BLACK)
arcade.draw_triangle_filled(355, 110, 355, 100, 373, 75, arcade.color.BLACK)
arcade.draw_triangle_filled(355, 90, 355, 82, 373, 58, arcade.color.BLACK)
arcade.draw_triangle_filled(344, 90, 346, 82, 335, 58, arcade.color.BLACK)

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



# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()