import random
import time
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window = None, seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.cells = []
        if seed != None:
            random.seed(seed)

        self.create_cells()
        self.break_entrance_and_exit()
        self.break_wall_r(0, 0)
        self.reset_cells_visited()
    
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
        time.sleep(0.04)

    def break_entrance_and_exit(self):
        self.cells[0][0].top_wall = False
        self.draw_cell(0, 0)

        self.cells[self.num_cols - 1][self.num_rows - 1].bottom_wall = False
        self.draw_cell(self.num_cols - 1, self.num_rows - 1)

    def break_wall_r(self, i, j):
        self.cells[i][j].visited = True

        counter = 0
        while counter <= 20:
            random_int = random.randint(1, 4)
            counter += 1
            if random_int == 1: #left
                if 0 < i and self.cells[i - 1][j].visited == False:
                    self.cells[i][j].left_wall = False
                    self.cells[i - 1][j].right_wall = False
                    self.break_wall_r(i - 1, j)

            elif random_int == 2: #down
                if j + 1 < self.num_rows and self.cells[i][j + 1].visited == False:
                    self.cells[i][j].bottom_wall = False
                    self.cells[i][j + 1].top_wall = False
                    self.break_wall_r(i, j + 1)

            elif random_int == 3: #right
                if i + 1 < self.num_cols and self.cells[i + 1][j].visited == False:
                    self.cells[i][j].right_wall = False
                    self.cells[i + 1][j].left_wall = False
                    self.break_wall_r(i + 1, j)
            else: # up
                if 0 < j and self.cells[i][j - 1].visited == False:
                    self.cells[i][j].top_wall = False
                    self.cells[i][j - 1].bottom_wall = False
                    self.break_wall_r(i, j - 1)

        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        self.cells[i][j].draw(x1, y1, x1 + self.cell_size_x, y1 + self.cell_size_y)
        self._animate()
    
    def reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.cells[i][j].visited = False

    def solve_dfs(self, i, j):
        self._animate()   

        self.cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        counter = 0
        while counter <= 100:
            random_int = random.randint(1, 4)
            counter += 1
            next = self.cells[i][j]
            dx = 0
            dy = 0
            if random_int == 1: #left
                if 0 < i and self.cells[i - 1][j].visited == False and self.cells[i][j].left_wall == False and self.cells[i - 1][j].right_wall == False:
                    next = self.cells[i - 1][j]
                    dx = -1

            elif random_int == 2: #down
                if j + 1 < self.num_rows and self.cells[i][j + 1].visited == False and self.cells[i][j].bottom_wall == False and self.cells[i][j + 1].top_wall == False:
                    next = self.cells[i][j + 1]
                    dy = 1


            elif random_int == 3: #right
                if i + 1 < self.num_cols and self.cells[i + 1][j].visited == False and self.cells[i][j].right_wall == False and self.cells[i + 1][j].left_wall == False:
                    next = self.cells[i + 1][j]
                    dx = 1

            else: # up
                if 0 < j and self.cells[i][j - 1].visited == False and self.cells[i][j].top_wall == False and self.cells[i][j - 1].bottom_wall == False:
                    next = self.cells[i][j - 1]
                    dy = -1
            
            if self.cells[i][j] != next:
                self.cells[i][j].draw_move(next)
                did_finish = self.solve_dfs(i + dx, j + dy)

                if did_finish == False:
                    self.cells[i][j].draw_move(next, True)

                else:
                    return

        return False

    def solve(self):
        return self.solve_dfs(0, 0)
