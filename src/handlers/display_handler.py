import pygame
from pygame import SurfaceType

from src.components.ball import Ball
from src.components.colors import Colors
from src.components.player import Player


class DisplayHandler:
    def __init__(self, display: SurfaceType):
        self.display = display

    def draw_start(self, player: Player, ball: Ball) -> None:
        self.display.fill(Colors.GRAY)
        pygame.display.set_caption("Brick Breaker Challenge")

        pygame.draw.rect(self.display, player.color, player.element)
        pygame.draw.rect(self.display, ball.color, ball.element)

    def draw_game_over(self):
        font = pygame.font.Font(None, 30)

        texto = font.render(f"Perdeu #Triste", 1, Colors.WHITE)
        self.display.blit(texto, (300, 300))
