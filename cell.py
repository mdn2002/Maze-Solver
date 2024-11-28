from graphics import Window, Point, Line

class Cell:
    def __init__(self, window = None):
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.window = window
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self.window == None:
            return
        
        self.x1 = x1
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        color = "black"
        if self.left_wall == False: 
            color = "#d9d9d9"
        self.window.draw_line(Line(Point(x1, y1), Point(x1, y2)), color)

        color = "black"
        if self.right_wall == False: 
            color = "#d9d9d9"
        self.window.draw_line(Line(Point(x2, y1), Point(x2, y2)), color)

        color = "black"
        if self.top_wall == False: 
            color = "#d9d9d9"
        self.window.draw_line(Line(Point(x1, y1), Point(x2, y1)), color)

        color = "black"
        if self.bottom_wall == False: 
            color = "#d9d9d9"
        self.window.draw_line(Line(Point(x1, y2), Point(x2, y2)), color)
    
    def draw_move(self, to_cell, undo=False):
        if self.window == None:
            return
        
        color = "red"
        if undo == True:
            color = "gray"
        
        self.window.draw_line(Line(Point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2), 
                                   Point((to_cell.x1 + to_cell.x2) / 2, (to_cell.y1 + to_cell.y2) / 2)), color)

        