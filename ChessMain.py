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
        IMAGES[piece] = pg.transform.scale(pg.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

    #Images can be accessed by saying 'IMAGES['wP']'
        
"""
The main driver for the code, handling user input and updating graphics
"""