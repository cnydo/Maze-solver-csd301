from Line import Line
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width: float , height: float) -> None:
        """Initialize the window
        Args:
            - width (float): width of the window
            - height (float): size of the window
        """
        # Creating a new window.
        self.__root = Tk()
        # Setting the title of the window to "Maze solver"
        self.__root.title("Maze solver")
        # Setting the size of the window.
        self.__root.geometry(f"{width}x{height}")
        # Making the window not resizable.
        self.__root.resizable(False, False)
        # A method that is called when the user closes the window.
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        # Creating a canvas with the given width and height.
        self.__canvas = Canvas(self.__root, width=width, height=height, bg='white')
        # Packing the canvas.
        self.__canvas.pack(fill=BOTH, expand=1)
        # Runnig state of the window.
        self.__running = False
        
    def redraw(self):
        """
        It forces the window to redraw itself
        """
        self.__root.update_idletasks()
        self.__root.update()
        
    def draw_line(self, line: Line, fill_color="black"):
        """
        It draws a line on the canvas.
        Args:
            - line (Line): A Line object
            - fill_color (str, optional): The color of the line, defaults to black (optional)
        """
        line.draw(self.__canvas, fill_color)
        
    def wait_for_close(self):
        """
        The function waits for the user to close the window
        """
        self.__running = True
        # A loop that keeps the window open until the user closes it.
        while self.__running:
            self.redraw()
        print("window closed...")
        
    def close(self):
        """
        It sets the value of the variable `__running` to `False`
        """
        self.__running = False
        