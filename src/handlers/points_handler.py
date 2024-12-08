import pygame
from pygame import SurfaceType

from src.components.colors import Colors
from src.handlers.blocks_handler import BlocksHandler


class PointsHandler:
    def __init__(self, display: SurfaceType, blocks_handler: BlocksHandler):
        self.display = display
        self.blocks_handler = blocks_handler

    def update(self):
        points = self.blocks_handler.blocks_count - len(self.blocks_handler.blocks)
        # print(self.blocks_handler.blocks_count, len(self.blocks_handler.blocks))

        font = pygame.font.Font(None, 30)
        texto = font.render(f"Pontuação: {points}", 1, Colors.BLACK)

        self.display.blit(texto, (0, 0))
        if points >= self.blocks_handler.blocks_count:
            return True
        else:
            return False
