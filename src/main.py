import curses

from scenes.game import Game
from scenes.title_screen import TitleScreen

from entities.board import Board

WIDTH = 10
HEIGHT = 20
X_OFFSET = 5
Y_OFFSET = 2

def run(stdscrn):
    main_window = curses.initscr()
    curses.resize_term(30, 100)

    curses.noecho()
    curses.curs_set(0)
    curses.start_color()
    main_window.keypad(1)

    title_screen = TitleScreen(main_window, X_OFFSET)

    board = Board(main_window, WIDTH, HEIGHT)
    tetris = Game(main_window, board)
    
    title_screen.run()
    tetris.run()

if __name__ == "__main__":
    curses.wrapper(run)
