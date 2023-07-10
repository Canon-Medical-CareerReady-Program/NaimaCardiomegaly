from Cardiomegaly.measurement import Measurement

def test_init():
    heart=Measurement()
    assert heart.distance()==0

    heart.end.x=100

    assert heart.distance()==100