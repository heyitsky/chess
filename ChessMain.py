"""
This is the main driver file, it will be repsonsible for handling user input and displaying the current GameState
"""

import pygame as pg
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8 #chessboard dimensions
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

"""
Initialise a global dictoinary of images. This will be called once in the main
"""

def load_images():
    pieces = ['wP', 'wR', 'wB', 'wN', 'wQ', 'wK', 'bP', 'bR', 'bB', 'bN', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load("assets/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

    #Images can be accessed by saying 'IMAGES['wP']'
        
"""
The main driver for the code, handling user input and updating graphics
"""

def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color("white"))
    game_state = ChessEngine.GameState()
    load_images() #only loading once, before the while loop
    running = True

    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
        draw_game_state(screen, game_state)
        clock.tick(MAX_FPS)
        pg.display.flip()

"""
Responsible for all graphics within the current game state
"""
def draw_game_state(screen, game_state):
    draw_board(screen) #draw squares on the board
    # same method for move suggestions, piece highlighting
    draw_pieces(screen, game_state.board) #draw pieces on top of sqaures

"""
Draw the squares on the board
"""
def draw_board(screen):
    colours = [pg.Color("dark green"), pg.Color("light blue")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            colour = colours[(row + column) % 2]
            pg.draw.rect(screen, colour, pg.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    
"""
Responsible for drawing the pieces on ht eboard using the game_state.board
"""
def draw_pieces(screen, board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--": #not empty
                screen.blit(IMAGES[piece], pg.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()
