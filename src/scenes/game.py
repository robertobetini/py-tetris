from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT
from .scene import Scene

class Game(Scene):
    __ESC = 27

    def __init__(self, screen, board):
        self.screen = screen
        self.board = board

    def __display(self):
        self.screen.refresh()
        self.board.display()

    def run(self):
        key = 0
        while key != self.__ESC:
            key = self.screen.getch()
            self.__display()
    