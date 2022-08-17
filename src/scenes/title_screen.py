import sys
import curses

from curses import panel, KEY_DOWN, KEY_UP
from .scene import Scene

class TitleScreen(Scene):
    MENU = ("Start", "Exit")

    def __display(self, screen, position):
        screen.addstr(1, 50, "--+= PyTetris =+--", curses.A_BOLD)

        for i, item in enumerate(self.MENU):
                mode = curses.A_NORMAL
                if i == position:
                    mode = curses.A_REVERSE
                screen.addstr(3 + i, 50, f'{i}. {item}', mode)

    def run(self, screen):
        ALTERNATIVE_KEY_DOWN = 456
        ALTERNATIVE_KEY_UP = 450

        position = 0
        _panel = panel.new_panel(screen)
        _panel.top()
        _panel.show()
        screen.clear()

        while True:
            screen.refresh()

            self.__display(screen, position)

            key = screen.getch()

            if key in (KEY_UP, ALTERNATIVE_KEY_UP):
                position = 0
            elif key in (KEY_DOWN, ALTERNATIVE_KEY_DOWN):
                position = len(self.MENU) - 1
            elif key in (curses.KEY_ENTER, ord("\n")):
                if position == len(self.MENU) - 1:
                    sys.exit()
                else:
                    screen.clear()
                    break

            curses.curs_set(0)

        screen.clear()
        _panel.hide()
        panel.update_panels()
        curses.doupdate()
