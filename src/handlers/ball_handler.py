from pygame import SurfaceType

from src.components.ball import Ball
from src.components.player import Player
from src.handlers.blocks_handler import BlocksHandler
from src.utils.errors import GameOverError


class BalHandler:
    def __init__(self, display: SurfaceType, player: Player, blocks_handler: BlocksHandler):
        self.start_position = [3, -3]
        self.position = self.start_position
        self.display = display
        self.player = player
        self.blocks_handler = blocks_handler

    def move(self, ball: Ball):
        if self.position is None:
            raise GameOverError()

        move = self.position

        print(move)

        ball.element.x = ball.element.x + move[0]
        ball.element.y = ball.element.y + move[1]

        if ball.element.x <= 0:
            move[0] = -move[0]
        if ball.element.y <= 0:
            move[1] = -move[1]
        if ball.element.x + 15 >= self.display.get_size()[0]:
            move[0] = -move[0]
        if ball.element.y + 15 >= self.display.get_size()[1]:
            self.position = None
            raise GameOverError()

        if self.player.element.collidepoint(ball.element.x, ball.element.y):
            move[1] = -move[1]
        for block in self.blocks_handler.blocks:
            if block.element.collidepoint(ball.element.x, ball.element.y):
                self.blocks_handler.blocks.remove(block)
                move[1] = -move[1]
        return move
