import pygame
from model.BoardModel import BoardModel, Tile
from model.MoveManager import MoveManager
from model.pieces import *
from model.constants import WHITE, BLACK

# importer tous les models ici, pour qu'ils soient disponibles dasn le controller (centralise)
class AppModel :
    def __init__(self) -> None:
        self.game_is_running = True
        self.sprites = pygame.sprite.Group()
        self.board = BoardModel()
        self.load_game()
       
        print("Game initialized")
        
    def load_game(self):
        self.over = False
        self.captured_piece = False
        self.last_piece_killed = None
        self.board.selected_tile = []
        self.board.all_possible_tiles = []
        self.sprites.empty()
        self.register_pieces()
        self.set_piece_tile()
        self.active_piece = None
        self.current_player = WHITE
        self.move_manager = MoveManager()
        print("Game loaded")
        
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
            
    def set_piece_tile(self):
        for piece in self.pieces:
            piece : Piece
            for tile in self.board.tiles :
                tile : Tile
                if not piece.pos == tile.coord :
                    continue
                else : 
                    piece.rect.topleft = tile.rect.topleft
                    self.sprites.add(piece)
                    
    def select_piece(self, pos):                   
        if self.active_piece is None :   
            for piece in self.pieces:
                piece : Piece
                if piece.rect.collidepoint(pos) and piece.color == self.current_player :    
                    # à partir d'ici j'ai la main sur la pièce selectionnée
                    self.active_piece = piece
                    self.move_manager.set_active_piece(self.active_piece)
                    self.board.selected_tile = piece.rect.copy()
                    self.board.illegal_tile = None
                    self.board.all_possible_tiles = None
                    
    # calculer ici l'état du plateau et 
    # faire des observateurs pour détecter quand pièce déplacée et donc changement joueur
    
    def drop_piece(self, pos) : 
        if self.active_piece is None:
            return
        
        for tile in self.board.tiles:
            tile : Tile
            if not tile.rect.collidepoint(pos):
                continue  # Passez à la prochaine pos si pas collision
            
        # faire check legal move ici
        
            self.active_piece.move(tile.rect, pos)
            self.active_piece = None
        
        