"""
Sprite move between different rooms.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_rooms
"""
import random
import arcade
import os

SPRITE_SCALING = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)
NUMBER_OF_COINS = 50
SCREEN_WIDTH = SPRITE_SIZE * 14
SCREEN_HEIGHT = SPRITE_SIZE * 10
SCREEN_TITLE = "Vault 76 Maze"

MOVEMENT_SPEED = 10

class Room:
    """
    This class holds all the information about the
    different rooms.
    """
    def __init__(self):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None

        # This holds the background images. If you don't want changing
        # background images, you can delete this part.
        self.background = None


def setup_room_1():
    """
    Create and return room 1.
    If your program gets large, you may want to separate this into different
    files.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up on the right side
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)
    # Walls for the interior of the box
    for y in range(475, 600, 50):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 150
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(0, 200, 50):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 350
        room.wall_list.append(wall)

    for y in range(0, 200, 50):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 150
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(200, 500, 50):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 275
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(580, 600, 50):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 275
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(300, 500, 50):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 400
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(300, 425, 50):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for y in range(96, 196, 50):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 400
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(96, 250, 50):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 525
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(400, 600, 50):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 525
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(400, 650, 50):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 450
        room.wall_list.append(wall)

    for y in range(225, 350, 50):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 675
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(700, 850, 50):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 225
        room.wall_list.append(wall)

    for y in range(0, 150, 50):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 760
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(275, 500, 50):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 720
        wall.center_y = y
        room.wall_list.append(wall)

    # Load the background image for this level.
    room.background = arcade.load_texture("city2.jpg")

    return room


def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x != 0:
                wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
    wall.left = 5 * SPRITE_SIZE
    wall.bottom = 6 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("city.jpg")

    for y in range(150, 600, 64):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 150
        wall.center_y = y
        room.wall_list.append(wall)
    for y in range(300, 450, 64):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 300
        wall.center_y = y
        room.wall_list.append(wall)
    for y in range(0, 160, 64):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 300
        wall.center_y = y
        room.wall_list.append(wall)
    for y in range(0, 275, 64):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 475
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(325, 450, 64):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 425
        room.wall_list.append(wall)
    for y in range(425, 600, 64):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 425
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(350, 500, 64):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 600
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(600, 850, 64):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 475
        room.wall_list.append(wall)

    for x in range(600, 850, 64):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 200
        room.wall_list.append(wall)

    for y in range(200, 350, 64):
        wall = arcade.Sprite("Iron_Block.png", SPRITE_SCALING)
        wall.center_x = 725
        wall.center_y = y
        room.wall_list.append(wall)

    return room


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.current_room = 0

        # Other Sprite variables
        self.coin_list = None
        self.score = 0
        self.wall_list = None

        # Set up the player
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite = arcade.Sprite("character_robot_talk.png", SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        self.coin_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.
        room = setup_room_1()
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

        # If you want coins or monsters in a level, then add that code here.
        for i in range(NUMBER_OF_COINS):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("pearl.png", SPRITE_SCALING_COIN)

            # --- IMPORTANT PART ---

            # Boolean variable if we successfully placed the coin
            coin_placed_successfully = False

            # Keep trying until success
            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True

            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.rooms[self.current_room].background)

        # Draw all the walls in this room
        self.rooms[self.current_room].wall_list.draw()

        # If you have coins or monsters, then copy and modify the line
        # above for each list.

        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
