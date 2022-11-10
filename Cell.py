from __future__ import annotations
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
        self._x1: float = None
        self._x2: float = None
        self._y1: float = None
        self._y2: float = None
        self._win: Window = win
        
    @property
    def x1(self) -> float:
        return self._x1
    
    @x1.setter
    def x1(self, value: float) -> None:
        self._x1 = value
        
    @property
    def x2(self) -> float:
        return self._x2
    
    @x2.setter
    def x2(self, value: float) -> None:
        self._x2 = value
        
    @property
    def y1(self) -> float:
        return self._y1
    
    @y1.setter
    def y1(self, value: float) -> None:
        self._y1 = value
        
    @property
    def y2(self) -> float:
        return self._y2
    
    @y2.setter
    def y2(self, value: float) -> None:
        self._y2 = value
        
    @property
    def win(self) -> Window:
        return self._win
    
    @win.setter
    def win(self, value: Window) -> None:
        self._win = value
        
    def draw(self, x1: float, y1: float, x2: float, y2: float) -> None:
        """
        The function draws the walls of the cell.
        
        Args:
            - x1 (float): The x coordinate of the top left corner of the cell
            - y1 (float): The y coordinate of the top left corner of the cell
            - x2 (float): The x coordinate of the bottom right corner of the cell
            - y2 (float): The y coordinate of the bottom right corner of the cell
        """
        if self._win is None:
            return
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
            
    def draw_move(self, other: Cell, undo=False) -> None:
        if self._win is None:
            return
        x_mid = (self._x1 + other._x2) / 2
        y_mid = (self._y1 + other._y2) / 2
        to_x_mid = (other._x1 + other._x2) / 2
        to_y_mid = (other._y1 + other._y2) / 2
        fill_color = "gray" if undo else "red"
        
        # move left 
        if self._x1 > other.x1:
            # draw line from midpoint of left wall to self center
            line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
            self._win.draw_line(line, fill_color)
            # draw line from other center to the midpoint of other's right wall
            line = Line(Point(to_x_mid, to_y_mid), Point(other.x2, to_y_mid))
            self._win.draw_line(line, fill_color)
        # move right
        elif self._x1 < other.x1:
            # draw line from center to midpoint of right wall
            line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
            self._win.draw_line(line, fill_color)
            # draw line from midpoint of other's left wall to other center
            line = Line(Point(other.x1, to_y_mid), Point(to_x_mid, to_y_mid))
        # move up
        elif self._y1 > other.y1:
            # draw line from midpoint of top wall to center
            line = Line(Point(x_mid, self._y1), Point(x_mid, y_mid))
            self._win.draw_line(line, fill_color)
            # draw line from other center to midpoint of other's bottom wall
            line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, other.y2))
            self._win.draw_line(line, fill_color)
        # move down
        elif self._y1 < other.y1:
            # draw line from center to midpoint of bottom wall
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
            self._win.draw_line(line, fill_color)
            # draw line from midpoint of other's top wall to other center
            line = Line(Point(to_x_mid, other.y1), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)
        