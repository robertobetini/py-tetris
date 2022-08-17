import curses

from curses import panel, KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT
from .scene import Scene

class Game(Scene):
    __ESC = 27

    def __init__(self, board):
        self.board = board

    def __display(self, screen):
        screen.refresh()
        self.board.display(screen)

    def run(self, screen):
        key = 0
        while key != self.__ESC:
            key = screen.getch()
            self.__display(screen)
    