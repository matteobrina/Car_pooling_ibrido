class Nodo:
    

    def __init__(self, x, y, c=0, i=0):
        self.x=x
        self.y=y
        self.c=c
        self.i=i

    def __str__(self):
        return("Node{" + "X=" + str(self.x) + " Y=" + str(self.y) + " C=" +str(self.c) + " ID=" +str(self.i) +"}")

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_c(self):
        return self.c
    def get_id(self):
        return self.i
    
    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y=y
    
    def set_c(self, c):
        self.c=c
    
    def set_id(self, i):
        self.i=i

        
    def __lt__(self, other):
        return self.c < other.c
    
    def __gt__(self, other):
        return self.c > other.c
    
        
    def __eq__(self, other):
        return self.c == other.c


    

    
