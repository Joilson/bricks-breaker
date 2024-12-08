from pygame import SurfaceType
from pygame.event import EventType
import pygame
from pygame.rect import RectType

from src.components.player import Player


class PlayerHandler:
    def __init__(self, display: SurfaceType):
        self.display = display

    def move(self, event: EventType, player: Player):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if (player.element.x + 100) < self.display.get_size()[0]:
                    player.element.x = player.element.x + 5
            if event.key == pygame.K_LEFT:
                if player.element.x > 0:
                    player.element.x = player.element.x - 5
