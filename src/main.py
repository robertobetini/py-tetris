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
    title_screen = TitleScreen(screen)

    board = Board(screen, 10, 20)
    tetris = Game(screen, board)

    os.system('mode con: cols=99 lines=25')
    
    title_screen.run()
    tetris.run()

if __name__ == "__main__":
    curses.wrapper(run)
