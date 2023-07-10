from coordinate import Coordinate
from math import sqrt

class Measurement:
    # start= Coordinate(0,0)
    # end= Coordinate(0,0)

    def __init__(self):
        self.clear()

    def distance(self):
        x1, y1= self.start.x, self.start.y
        x2, y2= self.end.x, self.end.y
        distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distance
    
    def clear(self):
        self.start= Coordinate(0,0)
        self.end= Coordinate(0,0)
