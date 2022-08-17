class Board:
    def __init__(self, window, width=10, height=20):
        self.window = window
        self.width = width
        self.height = height
        self.pieces = []

    def display(self):
        self.window.addstr(1, 1, "+----------+")

        for i in range(self.height):
            self.window.addstr(2 + i, 1, "|          |")

        self.window.addstr(2 + self.height, 1, "+----------+")
