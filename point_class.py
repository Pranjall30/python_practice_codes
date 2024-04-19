import math

class Point:
    def __init__(self,p1,p2,p3):
        self.p1=p1
        self.p2=p2
        self.p3=p3

    def get_distance(self, other_point):
        distance = math.sqrt((self.p1 - other_point.p1) ** 2 +
                             (self.p2 - other_point.p2) ** 2 +
                             (self.p3 - other_point.p3) ** 2 )
        return distance

point1 = Point(1,2,3)
point2 = Point(4,5,6)
if(distance1==distance2):
            print("Distance from origin is same")

else:
    print("Distance from origin is not same")