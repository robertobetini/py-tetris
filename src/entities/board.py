from entities.square_piece import SquarePiece

from .piece import Piece

class Board:
    def __init__(self, window, width=10, height=20):
        self.window = window
        self.width = width
        self.height = height
        self.active_piece = SquarePiece(window, 2, 2)
        self.pieces = []

    def display(self):
        self.window.addstr(1, 1, f"+{ self.width * '-' }+")

        for i in range(self.height):
            self.window.addstr(2 + i, 1, f"|{ self.width * ' ' }|")

        self.window.addstr(2 + self.height, 1, f"+{ self.width * '-' }+")

        self.active_piece.display()
        for piece in self.pieces:
            piece.display()

    def update(self):
        self.active_piece.drop()
