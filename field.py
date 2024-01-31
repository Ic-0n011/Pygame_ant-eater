import variables
from random import sample, randint
from game_objets import Anthill, Player

QUANTITY_ANTHILLS = randint(variables.MIN_ANTHILLS, variables.MAX_ANTHILLS)


class Field():
    """
    класс поле
    поле создает и(или) хранит:
    список клеток
    список с пустыми клетками
    муравейники
    муравьев
    игрока(муравьеда)
    """
    def __init__(self, img) -> None:
        self.rows = variables.ROWS
        self.cols = variables.COLS
        self.img_player = img
        self.anthills = []
        self.cells = []
        self.ants = []
        self.quantity_ants = 1
        self.score_points = 0
        self.player = Player(
            (variables.ROWS//2)+1, (variables.COLS//2)+1, self.img_player
                            )

    def creating_a_field(self, cell_surf) -> None:
        """создание поля"""
        for _ in range(variables.ROWS):
            row = [0] * self.cols
            self.cells.append(row)
        for y in range(self.rows):
            for x in range(self.cols):
                cell = Cell(y+1, x+1, cell_surf)
                self.cells[y][x] = cell

    def get_empty_cells(self, game) -> None:
        """создание листа с пустыми клетками"""
        self.empty_cells = []
        for row in self.cells:
            for cell in row:
                cell.cell_updater(game=game)
                if cell.content == variables.IMG_CELL:
                    self.empty_cells.append(cell)

    def create_anthills(self, game) -> None:
        """создание муравейников"""
        self.get_empty_cells(game)
        random_empty_cell = sample(self.empty_cells, QUANTITY_ANTHILLS)
        for cell in random_empty_cell:
            anthill = Anthill(cell.y, cell.x, game.img_anthill)
            self.anthills.append(anthill)
            self.quantity_ants += anthill.ants_inside

    def find_free_nearby_cells(self, game, x, y) -> list:
        """поиск рядом находящихся пустых клеток"""
        list_of_coords = []
        allowed_x = [x, x-1, x+1]
        allowed_y = [y, y-1, y+1]
        for row in self.cells:
            for cell in row:
                if (cell.x in allowed_x) and (cell.y in allowed_y):
                    if not (x == cell.x and y == cell.y):
                        cell.cell_updater(game)
                        if cell.content == variables.IMG_CELL:
                            list_of_coords.append(cell)
        return list_of_coords


class Cell():
    """
    класс клетка
    клеток в игре ROWS*COLS
    клетка может обновиться, знает что в ней лежит
    """
    def __init__(self, y, x, cell_surf) -> None:
        self.y = y
        self.x = x
        self.content = None
        self.img = cell_surf

    def cell_updater(self, game) -> None:
        """обновление внутреклеточного контента и картинки"""
        self.content = None
        if game.field.player.y == self.y and game.field.player.x == self.x:
            self.content = game.field.player.img
        for _ in range(QUANTITY_ANTHILLS):
            for anthill in game.field.anthills:
                if anthill.x == self.x and anthill.y == self.y:
                    self.content = anthill.img
                for ant in game.field.ants:
                    if ant.y == self.y and ant.x == self.x:
                        if self.content == game.field.player.img:
                            game.field.ants.remove(ant)
                            game.field.score_points += 1
                        else:
                            self.content = ant.img
        if not self.content:
            self.content = variables.IMG_CELL
