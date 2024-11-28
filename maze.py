import random
import time
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.cells = []

        self.create_cells()
        self.break_entrance_and_exit()
    
    def create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.window))
            self.cells.append(col_cells)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cell(i, j)
        
    def draw_cell(self, i, j):  
        if self.window is None:
            return
        
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        self.cells[i][j].draw(x1, y1, x1 + self.cell_size_x, y1 + self.cell_size_y)
        self._animate()

    def _animate(self):
        if self.window is None:
            return
        self.window.redraw()
        time.sleep(0.05)

    def break_entrance_and_exit(self):
        self.cells[0][0].top_wall = False
        self.draw_cell(0, 0)

        self.cells[self.num_cols - 1][self.num_rows - 1].bottom_wall = False
        self.draw_cell(self.num_cols - 1, self.num_rows - 1)