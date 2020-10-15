
import arcade
import random

# Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

SPRITE_SCALING = 0.2


# Class for all coin sprites
class Coin(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_y -= 1

        if self.top < 0:
            self.bottom = SCREEN_HEIGHT


# Class for all fire sprites
class Fire(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_x -= 1

        if self.right < 0:
            self.left = SCREEN_WIDTH


class MyApplication(arcade.Window):
    def __init__(self, width, height):

        super().__init__(width, height)

        # Empty variables
        self.all_sprite_list = None
        self.good_sprites = None
        self.bad_sprites = None

        self.player_sprite = None

        self.score = 0

        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BURNT_ORANGE)

        self.coin_sound = arcade.load_sound("Bottlecaps.ogg")

    # Setup, includes defined variables, player sprite, and player sprite position
    def setup(self):
        self.all_sprite_list = arcade.SpriteList()
        self.good_sprites = arcade.SpriteList()
        self.bad_sprites = arcade.SpriteList()

        self.score = 0
        # (Image from Scirra Forums, www.scirra.com)
        self.player_sprite = arcade.Sprite("../Lab 08 - Sprites/Vault_Boy.png", SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100

        self.all_sprite_list.append(self.player_sprite)

        # Draws coins in random locations
        for coin in range(75):
            # (Image from Key Word Suggest, keywordsuggest.org)
            coin = Coin("Nuka_Kola.png", SPRITE_SCALING )

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            self.all_sprite_list.append(coin)
            self.good_sprites.append(coin)

        # Draws fire in random locations
        for fire in range(45):
            # (Image from Icon Archive, www.iconarchive.com)
            fire = Fire("Deathclaw.png", SPRITE_SCALING )

            fire.center_x = random.randrange(SCREEN_WIDTH)
            fire.center_y = random.randrange(SCREEN_HEIGHT)

            self.all_sprite_list.append(fire)
            self.bad_sprites.append(fire)

    # Draws everything
    def on_draw(self):
        arcade.start_render()

        self.all_sprite_list.draw()
        arcade.draw_text("Player Score: " + str(self.score), 10, 20, arcade.color.WHITE, 24)

        if len(self.good_sprites) == 0:
            arcade.draw_text("GAME OVER", 230, 280, arcade.color.WHITE, 50)
            arcade.draw_text("SCORE: " + str(self.score), 240, 230, arcade.color.WHITE, 50)

    # Animates player sprite and continues animation only if good coins are present
    def animate(self, delta_time):
        if len(self.good_sprites) != 0:
            self.all_sprite_list.update()

        # Detects Collisions
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_sprites)
        for coin in hit_list:
            arcade.play_sound(self.coin_sound)
            coin.kill()
            self.score += 1

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_sprites)
        for fire in hit_list:
            fire.kill()
            self.score -= 1

    # Moves Player
    def on_mouse_motion(self, x, y, dx, dy):
        if len(self.good_sprites) != 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y


# Main Function
def main():
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()

    arcade.run()

main()