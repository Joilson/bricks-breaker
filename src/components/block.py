import pygame


class Block:
    def __init__(self, color: tuple[int, int, int], x: int, y: int, width: int = 90, height: int = 15):
        self.color = color
        self.element = pygame.Rect(
            x,
            y,
            width,
            height,
        )
