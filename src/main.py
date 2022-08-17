import curses

from scenes.game import Game
from scenes.title_screen import TitleScreen

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
curses.start_color()
screen.keypad(1)

def run(object):
    title_screen = TitleScreen()
    tetris = Game()

    title_screen.run(screen)
    tetris.run(screen)

if __name__ == "__main__":
    curses.wrapper(run)
