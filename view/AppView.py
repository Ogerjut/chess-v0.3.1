import pygame
from .BoardView import BoardView

class AppView : 
    def __init__(self, screen : pygame.Surface ) -> None:
        self.screen = screen
        self.board_view = BoardView(self.screen)
        print("UI initialized")
        
        
    # def render(self):
    #     self.board_view.draw()