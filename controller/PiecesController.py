from view import PiecesView
from model.pieces.piece import Piece

class PiecesController:
    def __init__(self, model : Piece, view : PiecesView) -> None:
        self.model = model
        self.view = view
        
        
    def render(self):
        self.view