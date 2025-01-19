import pygame
from .BoardView import BoardView
from .SpritesView import SpritesView

class AppView : 
    def __init__(self, screen : pygame.Surface ) -> None:
        self.screen = screen
        self.board_view = BoardView(self.screen)
        self.sprites_view = SpritesView(self.screen)
        
        print("UI initialized")
        
