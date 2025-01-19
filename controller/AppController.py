import pygame

from model.AppModel import AppModel
from view.AppView import AppView

from controller.BoardController import BoardController
from controller.SpriteController import SpritesController
from controller.EventController import EventController

class AppController : 
    def __init__(self, app : AppModel, ui : AppView) -> None:
        self.app_model = app
        self.app_view = ui
        
        self.board_controller = BoardController(self.app_model.board, self.app_view.board_view)
        self.sprite_controller = SpritesController(self.app_model, self.app_view.sprites_view)
        self.event_controller = EventController(self.app_model, self.app_view)
        
        print("Game controllers initialized")
        
   
        
    def handle_event(self, event : pygame.event.Event):
        # print(event)
        self.event_controller.handle_event(event)
    
    
    
    def render(self): 
        self.board_controller.render()
        self.sprite_controller.render()
        