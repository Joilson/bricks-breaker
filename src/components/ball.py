import pygame
from pygame.rect import RectType


class Ball:
    def __init__(self, color: tuple[int, int, int], len_x: int = 15, len_y: int = 15):
        self.element = pygame.Rect(100, 500, len_x, len_y)
        self.color = color
