import pygame
from model.BoardModel import Tile, BoardModel
from model.constants import BOARD_SIZE, TILE_PIXEL, X_OFFSET, Y_OFFSET
    
class BoardView:
    def __init__(self, screen : pygame.Surface) :
        self.screen = screen
        
        
    def draw(self, board : BoardModel):
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                rect = x*TILE_PIXEL + X_OFFSET, y*TILE_PIXEL + Y_OFFSET, TILE_PIXEL, TILE_PIXEL
                color = "Brown" if (x + y) % 2 == 1 else "White"
                pygame.draw.rect(self.screen, color, rect)
                self.draw_bordure(board)

    def draw_bordure(self, board : BoardModel ):
        for tile in board.tiles :
            tile : Tile
            rect = tile.rect
            pygame.draw.rect(self.screen, "Gold", rect, width=1)
            
            if board.selected_tile and rect == board.selected_tile :
                pygame.draw.rect(self.screen, "Blue", rect, width=2)
                
            if board.possible_tiles and tile.coord in board.possible_tiles : 
                pygame.draw.rect(self.screen, "Green", rect, width=2)
                
            if  board.all_possible_tiles and tile.coord in board.all_possible_tiles :
                pygame.draw.rect(self.screen, "Purple", rect, width=2)
                
            if board.illegal_tile and rect == board.illegal_tile  :
                pygame.draw.rect(self.screen, "Red", rect, width=2)
                
        