class ScratchCat:
    def __init__(self, screen_size):
        self.__screen_size = screen_size
        self.__width = 96
        self.__height = 101
        self.__pos_x = self.__screen_size[0] // 2 - self.__width // 2
        self.__pos_y = self.__screen_size[1] // 2 - self.__height // 2
        self.__costume = "cat1"
        self.__direction = "right"

    def pos(self):
        return self.__pos_x, self.__pos_y

    def direction(self):
        return self.__direction

    def on_edge(self):
        if self.__pos_x >= self.__screen_size[0] - self.__width:
            self.__direction = "left"
            return True
        elif self.__pos_x <= 0:
            self.__direction = "right"
            return True
        return False

    def move(self, steps):
        if self.__direction == "right":
            self.__pos_x += steps
        else:
            self.__pos_x -= steps

    def switch_costume(self):
        if self.__costume == "cat1":
            self.__costume = "cat2"
        else:
            self.__costume = "cat1"

    def costume(self):
        return self.__costume
