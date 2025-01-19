
import pygame

from model.AppModel import AppModel
from view.AppView import AppView

class EventController:
    def __init__(self, app : AppModel, ui : AppView) -> None:
        self.app = app
        self.ui = ui
    
    def handle_event(self, event : pygame.event.Event):
        if self.app.game_is_running : 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                self.app.select_piece(pygame.mouse.get_pos())
                
            if event.type == pygame.MOUSEMOTION :
                if self.app.active_piece is not None : 
                    self.app.active_piece.rect.move_ip(event.rel)
                            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 :
                    self.app.drop_piece(pygame.mouse.get_pos())