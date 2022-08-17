import sys
import curses

from curses import KEY_DOWN, KEY_UP, panel
from .game import Game

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
curses.start_color()
screen.keypad(1)
_panel = panel.new_panel(screen)

tetris = Game()

MENU = ("Start", "Exit")

def display():
    ALTERNATIVE_KEY_DOWN = 456
    ALTERNATIVE_KEY_UP = 450

    position = 0
    _panel.top()
    _panel.show()
    screen.clear()

    screen.addstr(1, 50, "--+= PyTetris =+--", curses.A_BOLD)

    while True:
        screen.refresh()

        for i, item in enumerate(MENU):
            mode = curses.A_NORMAL
            if i == position:
                mode = curses.A_REVERSE
            screen.addstr(3 + i, 50, f'{i}. {item}', mode)

        key = screen.getch()

        if key in (KEY_UP, ALTERNATIVE_KEY_UP):
            position = 0
        elif key in (KEY_DOWN, ALTERNATIVE_KEY_DOWN):
            position = len(MENU) - 1
        elif key in (curses.KEY_ENTER, ord("\n")):
            if position == len(MENU) - 1:
                sys.exit()
            else:
                screen.clear()
                break

        curses.curs_set(0)

    screen.clear()
    _panel.hide()
    panel.update_panels()
    curses.doupdate()

def run(object):
    display()
    tetris.run()

if __name__ == '__main__':
    curses.wrapper(run)
