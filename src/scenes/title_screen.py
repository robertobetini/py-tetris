import sys
import curses

from curses import panel, KEY_DOWN, KEY_UP
from .scene import Scene

class TitleScreen(Scene):
    MENU = ("Start", "Exit")

    __ALTERNATIVE_KEY_DOWN = 456
    __ALTERNATIVE_KEY_UP = 450

    __selected_position = 0

    def __init__(self, window, x_offset):
        self.window = window
        self.__x_offset = x_offset

    def run(self):
        title_screen_panel = panel.new_panel(self.window)
        title_screen_panel.top()
        title_screen_panel.show()
        self.window.clear()

        while True:
            self.__display()

            key = self.window.getch()
            if self.__is_user_ready(key):
                break

        curses.curs_set(0)
        self.window.clear()
        title_screen_panel.hide()
        panel.update_panels()
        curses.doupdate()

    def __display(self):
        self.window.refresh()
        self.window.addstr(1, self.__x_offset, "--+= PyTetris =+--", curses.A_BOLD)

        for i, item in enumerate(self.MENU):
                mode = curses.A_NORMAL
                if i == self.__selected_position:
                    mode = curses.A_REVERSE
                self.window.addstr(3 + i, self.__x_offset, f'{i}. {item}', mode)

    def __is_user_ready(self, key):
        if key in (KEY_UP, self.__ALTERNATIVE_KEY_UP):
            self.__selected_position = 0
        elif key in (KEY_DOWN, self.__ALTERNATIVE_KEY_DOWN):
            self.__selected_position = len(self.MENU) - 1
        elif key in (curses.KEY_ENTER, ord("\n")):
            if self.__selected_position == len(self.MENU) - 1:
                sys.exit()
            else:
                return True
