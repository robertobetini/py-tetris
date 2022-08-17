from .piece import Piece

class SquarePiece(Piece):
    def __init__(self, window, x_offset, y_offset):
        super().__init__(window, x_offset, y_offset)
        self.area = [
            [ self.PIECE_CENTER, self.SOLID_BLOCK ],
            [ self.SOLID_BLOCK, self.SOLID_BLOCK ]
        ]