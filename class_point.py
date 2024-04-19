class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,p):
        return ((self.x-p.x)**2 + (self.y-p.y)**2)**0.5
p1=point(3,4)
p2=point(6,8)
print(p1.distance(p2))