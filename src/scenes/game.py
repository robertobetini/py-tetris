from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT
from .scene import Scene

class Game(Scene):
    __ESC = 27

    def __init__(self, window, board):
        self.window = window
        self.board = board

    def run(self):
        key = 0
        while key != self.__ESC:
            key = self.window.getch()
            self.__display()

    def __display(self):
        self.window.refresh()
        self.board.display()
