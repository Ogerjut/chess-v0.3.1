import pygame
from model.pieces.piece import Piece

# ici toute la logique pour vérifier qu'un coup est légal
# qu'un roi est echec ou mat

# calculer l'état du plateau à chaque move  = coups possibles
class MoveManager:
    def __init__(self) -> None:
        self.active_piece = None
    
    def set_init_tile(self):
        self.init_rect = self.active_piece.rect.copy
        self.init_coord = self.active_piece.pos
    
    def set_active_piece(self, piece : Piece):
        self.active_piece = piece
        self.set_init_tile()
        