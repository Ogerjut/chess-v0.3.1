import pygame
from dataclasses import dataclass
from model.constants import BOARD_SIZE, TILE_PIXEL, X_OFFSET, Y_OFFSET


@dataclass
class Tile:
    coord : pygame.Vector2
    rect : pygame.Rect
    
class BoardModel:
    def __init__(self) :
        self.tiles = []
        self.selected_tile = None
        self.illegal_tile = None
        self.possible_tiles = None
        self.all_possible_tiles = None
        
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                rect = pygame.Rect(x * TILE_PIXEL + X_OFFSET, y * TILE_PIXEL + Y_OFFSET, TILE_PIXEL, TILE_PIXEL)
                coord = pygame.Vector2(x, y)
                tile = Tile(coord, rect)
                self.tiles.append(tile)
        # print(self.tiles)