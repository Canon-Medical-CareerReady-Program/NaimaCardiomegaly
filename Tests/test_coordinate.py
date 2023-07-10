from Cardiomegaly.coordinate import Coordinate

def test_init():
    start = Coordinate(0, 0)
    assert start.x==0
    assert start.y ==0

    start.x = 1
    start.y = 2

    assert start.x == 1
    assert start.y == 2
