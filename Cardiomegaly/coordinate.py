class Coordinate:

    def __init__(self, x , y):
        self.x=x
        self.y=y

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Coordinate(self.x * scalar, self.y * scalar)
        else:
            raise TypeError("Unsupported operand type for multiplication")

    def __rmul__(self, scalar):
        return self.__mul__(scalar)        

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Coordinate(self.x / scalar, self.y / scalar)
        else:
            raise TypeError("Unsupported operand type for division")