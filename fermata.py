import copy
class Fermata:

    def __init__(self, x, y, l):
        self.x=x
        self.y=y
        self.l=l

    def __str__(self):
        return("Fermata{" + "X=" + str(self.x) + " Y=" + str(self.y) +" Linea=" +str(self.l) +"}")

    def get_x(self):
        return copy.deepcopy(self.x)
    def get_y(self):
        return copy.deepcopy(self.y)
    def get_l(self):
        return copy.deepcopy(self.l)
    
    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y=y
    
    def set_l(self, l):
        self.l=l