
import pygame
from model.AppModel import AppModel

class SpritesView : 
    def __init__(self, screen : pygame.Surface ) -> None:
        self.screen = screen
        
    def render(self, app : AppModel) :
        app.sprites.draw(self.screen)