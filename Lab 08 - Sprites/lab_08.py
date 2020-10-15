""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.2
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_DEATHCLAW = 0.2
COIN_COUNT = 50
DEATHCLAW_COUNT = 25
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Coin(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()

    # Class for all fire sprites
    class Deathclaw(arcade.Sprite):
        def reset_pos(self):
            # Reset the coin to a random spot above the screen
            self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)

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

        arcade.set_background_color(arcade.color.AMAZON)

        self.coin_sound = arcade.load_sound("Bottlecaps.ogg")

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.deathclaw_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("Vault_Boy.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for coin in range(75):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin("Nuka_Kola.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        for deathclaw in range(45):

            deathclaw = deathclaw("Deathclaw.png", SPRITE_SCALING_DEATHCLAW)

            # Position the coin
            deathclaw.center_x = random.randrange(SCREEN_WIDTH)
            deathclaw.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.deathclaw_list.append(deathclaw)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.deathclaw_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.player_list) == 0:
            arcade.draw_text("GAME OVER", 230, 280, arcade.color.WHITE, 50)
            arcade.draw_text("SCORE: " + str(self.score), 240, 230, arcade.color.WHITE, 50)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        if len(self.player_list) != 0:
            self.coin_list.update()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            coin.reset_pos()
            self.score += 1

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.deathclaw_list)
        for deathclaw in hit_list:
            deathclaw.kill()
            self.score -= 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()