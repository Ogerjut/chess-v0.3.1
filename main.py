import pygame
import sys

from model import AppModel
from view import AppView
from controller import AppController
# from core import MainMenuState, OptionsState, PlayChessState

SCREEN_SIZE = ((800,800))
VERSION = '0.3.1'
FPS = 30

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(f"Chess game {VERSION}")
        print(f"Chess game {VERSION}")
        
        self.is_running = True
        self.clock = pygame.time.Clock()
        
        self.model = AppModel()
        self.view = AppView(self.screen)
        self.controller = AppController(self.model, self.view)
        
        # self.state = MainMenuState()
        
    def set_state(self, state):
        self.state = state

    # @property
    # def state(self) :
    #     return self._state
    
    # @state.setter
    # def set_state(self, value):
    #     self._state = value

    def run(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                
                self.controller.handle_event(event)

            # self.state.render(self)
            self.controller.render()
            pygame.display.flip()
            self.clock.tick(FPS)

    def exit(self):
        self.is_running = False
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    app = App()
    app.run()
