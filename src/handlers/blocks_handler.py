import pygame
from pygame import SurfaceType
from pygame.rect import RectType

from src.components.block import Block
from src.components.colors import Colors


class BlocksHandler:
    blocks: list[Block]

    def __init__(self, display: SurfaceType, blocks_by_rows=8, blocks_rows_len=5):
        self.display = display
        self.blocks_by_rows = blocks_by_rows
        self.blocks_rows_len = blocks_rows_len
        self.blocks_count = blocks_by_rows * blocks_rows_len

        self.__build_blocks()

    def __build_blocks(self):
        display_width = self.display.get_size()[0]
        blocks_distance = 5
        block_width = display_width / 8 - blocks_distance
        block_height = 15
        rows_distance = block_height + 10

        blocks = []
        for row_number in range(2, self.blocks_rows_len + 2):
            for col_number in range(self.blocks_by_rows):
                blocks.append(
                    Block(Colors.RED_1,
                          int(col_number * (block_width + blocks_distance)),
                          row_number * rows_distance
                          )
                )

        self.blocks = blocks

    def show_blocks(self):
        for block in self.blocks:
            pygame.draw.rect(self.display, block.color, block.element)
