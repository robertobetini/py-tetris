class Board:
    def __init__(self, screen, width=10, height=20):
        self.screen = screen
        self.width = width
        self.height = height

    def display(self):
        self.screen.addstr(1, 60, "+----------+")

        for i in range(self.height):
            self.screen.addstr(2 + i, 60, "|          |")

        self.screen.addstr(2 + self.height, 60, "+----------+")