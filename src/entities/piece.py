from .math.point import Point

class Piece:
    PIECE_CENTER = 2
    SOLID_BLOCK = 1
    EMPTY_BLOCK = 0
    PIECE_CHAR = "x"

    def __init__(self, window, x_offset, y_offset):
        self.window = window
        self.__x_offset = x_offset
        self.__y_offset = y_offset
        self.position = Point(x_offset, y_offset)
        self.area = [
            [self.PIECE_CENTER]
        ]

    def drop(self):
        self.position.y += 1

    def move_right(self):
        self.position.x += 1

    def move_left(self):
        self.position.x -= 1

    def display(self):
        self.window.addstr(self.position.y, self.position.x, self.PIECE_CHAR)

        for i in range(len(self.area)):
            for j in range(len(self.area[i])):
                block = self.area[i][j]

                if self.__is_solid(block):
                    self.window.addstr(self.position.y + i, self.position.x + j, self.PIECE_CHAR)

    def __is_solid(self, block):
        if block == self.PIECE_CENTER or block == self.SOLID_BLOCK:
            return True

        return False
