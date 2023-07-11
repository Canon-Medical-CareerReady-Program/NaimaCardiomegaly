from measurement import Measurement

class Result:
    def __init__(self):
       self.heart = Measurement()
       self.thorax = Measurement()

    def calculate_ratio(self):
        ratio= self.heart.distance() / self.thorax.distance()
        return ratio
    
    def calculate_percentage(self):
        percentage= self.calculate_ratio()*100
        return percentage
    
    def symptomatic(self):
        symptomatic = self.calculate_ratio() >0.5
        return symptomatic




