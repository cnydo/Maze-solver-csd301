from Line import Line
from Point import Point
from Window import Window

class Cell:
    def __init__(self, win: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        
    def draw(self, x1: float, y1: float, x2: float, y2: float):
        """
        The function draws the walls of the cell.
        
        Args:
            - x1 (float): The x coordinate of the top left corner of the cell
            - y1 (float): The y coordinate of the top left corner of the cell
            - x2 (float): The x coordinate of the bottom right corner of the cell
            - y2 (float): The y coordinate of the bottom right corner of the cell
        """
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        # Drawing left wall
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        # Drawing top wall
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        # Drawing right wall
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        # Drawing bottom wall
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)