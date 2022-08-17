import curses

from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT
from time import sleep
from threading import Thread

from .scene import Scene

class Game(Scene):
    __ESC = 27

    def __init__(self, window, board):
        self.__ticks = 0
        self.__difficulty = 1

        self.window = window
        self.board = board
        self.last_pressed_key = 0

        self.window.nodelay(True)

    def run(self):

        while self.last_pressed_key != self.__ESC:
            self.__handle_piece_movement()

            self.__display()
            if self.__ticks % (10 - self.__difficulty) == 0:
                self.__update()

            self.__ticks += 1
            sleep(0.05)

    def __handle_piece_movement(self):
        self.last_pressed_key =  self.window.getch()

        if self.last_pressed_key == KEY_RIGHT:
            self.board.active_piece.move_right()
        elif self.last_pressed_key == KEY_LEFT:
            self.board.active_piece.move_left()
        if self.last_pressed_key == KEY_DOWN:
            self.board.update()

    def __display(self):
        self.window.refresh()
        self.board.display()

    def __update(self):
        self.board.update()
