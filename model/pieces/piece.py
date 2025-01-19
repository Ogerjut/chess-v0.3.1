import pygame

# from pieces import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.sprite_sheet = pygame.image.load('asset/pieces_sprite.png').convert_alpha()
        self.sprite_sheet = pygame.transform.scale(self.sprite_sheet, (384, 128))
        
    def get_image(self, x, y): 
        image= pygame.Surface([64, 64], pygame.SRCALPHA)
        image.blit(self.sprite_sheet, (0,0),(x,y, 64, 64)) 
        return image
        
class Piece(Sprite) : 
    def __init__(self, x, y, coord, color, rule_move):
        super().__init__()
        self.image = self.get_image(x,y)
        self.rect = self.image.get_rect()
        self.pos = pygame.Vector2(coord)
        self.color = color
        self.rule_move = rule_move
        self.possible_moves = []
        
    def move(self, rect : pygame.Rect, coord : pygame.Vector2):
        self.pos = coord
        self.rect.topleft = rect.topleft
        
    
    # revoir le calcul des coord avec les vecteurs, retourne un Vector2 et non tuple
    def calculate_coord(self, pos, move) -> tuple :
        return (pos[0]+ move[0], pos[1]+move[1])
    
    def calculate_coord_i(self, pos, move, i) -> tuple :
        return (pos[0]+ i*move[0], pos[1]+i*move[1])
    
    def coord_in_board(self, coord : pygame.Vector2):
        if 8 > coord.x >= 0 and 8 > coord.y >=0 : 
            return True
        return False
    
    def get_piece_direction(self, line : bool, diag : bool) -> list : 
        directions = []        
        if line :
            directions.extend(((1, 0),(-1, 0),(0, 1),(0, -1)))
        if diag : 
            directions.extend(((1, 1),(1, -1),(-1, -1),(-1, 1)))
        return directions
    
    
    # à refaire, avec vector2 plus facile
    def get_move_direction(self, pos, coord):
        dx= coord[0]-pos[0]
        dy= coord[1]-pos[1]
        dx_normalized = 0 if dx == 0 else dx // abs(dx)
        dy_normalized = 0 if dy == 0 else dy // abs(dy)
    
        return (dx_normalized, dy_normalized)
        
        
        
    

        
        
