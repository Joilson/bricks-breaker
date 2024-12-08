import pygame
from pygame.rect import RectType


class Player:
    def __init__(self, color: tuple[int, int, int], len_x: int = 100, len_y: int = 15):
        self.element = pygame.Rect(0, 750, len_x, len_y)
        self.color = color
