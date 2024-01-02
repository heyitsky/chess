"""
This class is responsible for storing all of the information about the current state of the chess game. It will also be responsible for determining the valid moves at any current state. Will keep a move log.
"""

class GameState():
    def __init__(self):
        #board is an 8x8 2d list, each element of the list has 2 chars.
        #The first char represents the colour of the piece ('b' or 'w')
        #The second character represents the typw of the piece ('K', 'Q' etc.)
        #"--" represents an emtpy space with no piece.

        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.white_to_move = True
        self.move_log = []
