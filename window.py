from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height) -> None:
        """Initialize the window
        Args:
            width (int): width of the window
            height (int): size of the window
        """
        # Creating a new window.
        self._root = Tk()
        # Setting the title of the window to "Maze solver"
        self._root.title("Maze solver")
        # Setting the size of the window.
        self._root.geometry(f"{width}x{height}")
        # Making the window not resizable.
        self._root.resizable(False, False)
        # A method that is called when the user closes the window.
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        # Creating a canvas with the given width and height.
        self._canvas = Canvas(self._root, width=width, height=height, bg='white')
        # Packing the canvas.
        self._canvas.pack(fill=BOTH, expand=1)
        # Runnig state of the window.
        self._running = False
        
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()
        
    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()
        print("window closed...")
        
    def close(self):
        self._running = False