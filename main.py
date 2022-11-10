from Window import Window
from Point import Point
from Line import Line

def main():
    win = Window(800, 600)
    p1 = Point
    l = Line(Point(50, 50), Point(400, 400))
    win.draw_line(l, 'black')
    win.wait_for_close()
    
if __name__ == '__main__':
    main()