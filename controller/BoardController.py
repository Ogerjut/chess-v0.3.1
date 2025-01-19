from model.BoardModel import BoardModel
from view.BoardView import BoardView

class BoardController:
    def __init__(self, model : BoardModel, view : BoardView) -> None:
        self.model = model
        self.view = view
        
        
    def render(self): 
        self.view.draw(self.model)