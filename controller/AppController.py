import pygame

from model.AppModel import AppModel
from view.AppView import AppView

from controller.BoardController import BoardController
from PiecesController import PiecesController

class AppController : 
    def __init__(self, app : AppModel, ui : AppView) -> None:
        self.app_model = app
        self.app_view = ui
        
        self.board_controller = BoardController(self.app_model.board, self.app_view.board_view)
        # self.sprites_controller = PiecesController(self.app_model.sprites, self.app_view)
        print("Game controller initialized")
        
   
        
    def handle_event(self, event):
        # print(event)
        pass
    
    def render(self): 
        self.board_controller.render()
        