# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - магазин

CELL_TYPES = '🟩🌲🌊🏥🛒'


class Map:

    def print_map(self):
        """
        генератор карты
        """
        print('⬛' * (self.w + 2))
        for row in self.cells:
            print('⬛', end='')
            for cell in row:
                if 0 <= cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end='')
            print('⬛')
        print('⬛' * (self.w + 2))

    # def generate_rivers(self):
    #
    def generate_forest(self, r, mxr):
        for ri in self.h:
            for ci in self.w:
                #
                self.cells[ri][ci] = 1

    def check_bounds(self, x, y):
        if x < 0 or y < 0 or x >= self.h or y >= self.w:
            return False
        return True

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]


tmp = Map(10, 10)
tmp.print_map()
