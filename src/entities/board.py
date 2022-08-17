class Board:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height

    def display(self, screen):
        screen.addstr(1, 60, "+----------+")

        for i in range(self.height):
            screen.addstr(2 + i, 60, "|          |")

        screen.addstr(2 + self.height, 60, "+----------+")