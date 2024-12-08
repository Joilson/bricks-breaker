import pygame

from src.components.ball import Ball
from src.components.colors import Colors
from src.components.player import Player
from src.handlers.ball_handler import BalHandler
from src.handlers.blocks_handler import BlocksHandler
from src.handlers.display_handler import DisplayHandler
from src.handlers.player_handler import PlayerHandler
from src.handlers.points_handler import PointsHandler
from src.utils.errors import GameOverError

pygame.init()

is_end = False

SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
display = pygame.display.set_mode((800, 800), SURFACE)

ball = Ball(Colors.BLACK)
player = Player(Colors.BLACK)

display_handler = DisplayHandler(display)
blocks_handler = BlocksHandler(display)
ball_handler = BalHandler(display, player, blocks_handler)
points_handler = PointsHandler(display, blocks_handler)
player_handler = PlayerHandler(display)

while not is_end:
    try:
        display_handler.draw_start(player, ball)
        blocks_handler.show_blocks()
        is_end = points_handler.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_end = True

        player_handler.move(event, player)

        ball_handler.move(ball)
        pygame.time.wait(1)
        pygame.display.flip()
    except GameOverError:
        display_handler.draw_game_over()
        is_end = True

pygame.quit()
