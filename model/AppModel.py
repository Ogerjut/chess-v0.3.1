import pygame
from model.BoardModel import BoardModel
from pieces import *

# importer tous les models ici, pour qu'ils soient disponibles dasn le controller (centralise)
class AppModel :
    def __init__(self) -> None:
        self.game_is_running = False
        self.sprites = pygame.sprite.Group()
        self.board = BoardModel() 
        
        print("Game initialized")
        
        
    def register_pieces(self):
        self.pieces = [
            King(0 ,0, (4,7), "white"),
            Queen(64 ,0, (3,7), "white"),
            Bishop(128 ,0, (2,7), "white"),
            Knight(192 ,0, (1,7), "white"),
            Bishop(128 ,0, (5,7), "white"),
            Knight(192 ,0, (6,7), "white"),
            Rook(256 ,0, (0,7), "white"),
            Rook(256 ,0, (7,7), "white"),
            King(0 ,64, (4,0), "black"),
            Queen(64 ,64, (3,0), "black"),
            Bishop(128 ,64, (2,0), "black"),
            Knight(192 ,64, (1,0), "black"),
            Bishop(128 ,64, (5,0), "black"),
            Knight(192 ,64, (6,0), "black"),
            Rook(256 ,64, (0,0), "black"),
            Rook(256 ,64, (7,0), "black")
        ]
        for i in range(0,8):
            self.pieces.append(Pawn(320,0, (i,6), "white"))
            self.pieces.append(Pawn(320,64, (i,1), "black"))
            
            
    