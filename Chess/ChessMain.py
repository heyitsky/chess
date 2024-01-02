"""
This is the main driver file, it will be repsonsible for handling user input and displaying the current GameState
"""

import pygame as pg
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8 #chessboard dimensions
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}
