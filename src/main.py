import curses
import os

from scenes.game import Game
from scenes.title_screen import TitleScreen

from entities.board import Board

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
curses.start_color()
screen.keypad(1)

def run(object):
    title_screen = TitleScreen()

    board = Board(10, 20)
    tetris = Game(board)

    os.system('mode con: cols=99 lines=25')
    
    title_screen.run(screen)
    tetris.run(screen)

if __name__ == "__main__":
    curses.wrapper(run)
