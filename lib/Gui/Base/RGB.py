class RGB:
    def __init__(self, r: int, g: int, b: int):
        self.red = int(r)
        self.green = int(g)
        self.blue = int(b)

    def get(self, t: type = list):
        return t([self.red, self.green, self.blue])

    def add_color(self, r: int, g: int, b: int):
        self.red += int(r)
        self.green += int(g)
        self.blue += int(b)
