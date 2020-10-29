""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50
DEATHCLAW_COUNT = 20
SPRITE_SCALING_DEATHCLAW = 0.4
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Deathclaw(arcade.Sprite):

    def reset_pos(self):

        # Reset the deathclaw to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT)
        self.center_x = random.randrange(SCREEN_WIDTH + 10,
                                         SCREEN_WIDTH + 300)

    def update(self):

        # Move the deathclaw
        self.center_x -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.right< 0:
            self.reset_pos()


class Coin(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH + 100)

    def update(self):

        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.deathclaw = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color. GRAY)

        #play sounds
        #https://www.youtube.com/watch?v=2GIP80fM2Bo
        #https://www.youtube.com/watch?v=XH_ILMre9h8
        self.bottlecaps_sound = arcade.load_sound("Bottlecaps.ogg.")
        self.roar_sound = arcade.load_sound("roar.ogg")
    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.deathclaw_list = arcade.SpriteList()
        # Score
        self.score = 0

        # Set up the player
        # Character image from https://www.pngkit.com/
        self.player_sprite = arcade.Sprite("Vault_Boy.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the ENEMY
        for i in range(DEATHCLAW_COUNT):

            # Create the ENEMY instance
            # ENEMY image from https://fallout.fandom.com/
            deathclaw = Deathclaw("Deathclaw.png", SPRITE_SCALING_DEATHCLAW)

            # Position the coin
            deathclaw.center_x = random.randrange(SCREEN_WIDTH)
            deathclaw.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.deathclaw_list.append(deathclaw)

        for i in range(COIN_COUNT):

            # Create the Nuka Cola instance
            # Nuka Cola image fromh https://www.cleanpng.com/free/nuka-cola.html
            coin = Coin("Nuka_Kola.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.deathclaw_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.deathclaw_list.update()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            arcade.play_sound(self.bottlecaps_sound)
            coin.reset_pos()
            self.score += 1

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.deathclaw_list)
        for deathclaw in hit_list:
            arcade.play_sound(self.roar_sound)
            deathclaw.reset_pos()
            self.score -= 5


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

