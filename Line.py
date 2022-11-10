from tkinter import BOTH, Canvas
from Point import Point

class Line:
    def __init__(self, point1: Point, point2: Point) -> None:
        self.__point1 = point1
        self.__point2 = point2
    
    @property
    def point1(self) -> Point:
        return self.__point1
    
    @point1.setter
    def point1(self, point1: Point) -> None:
        self.__point1 = point1
        
    @property
    def point2(self) -> Point: 
        return self.__point2
    
    @point2.setter
    def point2(self, point2: Point) -> None:
        self.__point2 = point2
        
    def draw(self, canvas: Canvas, fill_color="black"):
        """It creates a line on the canvas, using the coordinates of the two points, and the fill color
        
        Args:
            - canvas (Canvas): The canvas on which to draw the line
            - fill_color (str, optional): The color of the line, defaults to black (optional)
        """
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill=fill_color,width=2
        )
        canvas.pack(fill=BOTH, expand=1)
        