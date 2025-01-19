# from model.AppModel
from view.SpritesView import SpritesView
from model.AppModel import AppModel

class SpritesController :
    
    def __init__(self, model : AppModel , view : SpritesView) -> None:
        self.model = model
        self.view = view
        
    def render(self): 
        self.view.render(self.model)