class Point:
    def __init__(self, x: float, y: float) -> None:
        """
        This function takes in two arguments, x and y, and sets the x and y attributes of the object to
        the values of the arguments
        
        Args:
            - x (float): The x coordinate of the point
            - y (float): The target variable
        """
        self.__x = x
        self.__y = y
        
    @property
    def x(self) -> float:
        """
        This function returns the x attribute of the object
        
        Returns:
            - float: The x attribute of the object
        """
        return self.__x
    
    @x.setter
    def x(self, x: float) -> None:
        """
        This function sets the x attribute of the object to the value of the argument
        
        Args:
            - x (float): The new value of the x attribute
        """
        self.__x = x
        