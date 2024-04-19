# class complex:
#     def __init__(self,x,y):
#         self.__x=x
#         self.__y=y
#     def add(self):  
#         return self.x+self.y
#     def get_x(self):
#         return self.__x
# c = complex(1,2)
# print(c.get_x() )



class complex:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    def sub(self):  
        return self.x-self.y
    def get_x(self):
        return self.__x
c = complex(1,2)
print(c.get_x() )