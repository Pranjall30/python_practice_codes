class employee:
    def __init__(self,id,deft,salary):
        self.id=id
        self.deft=deft
        self.salary=salary
    def get_tax(self):
        return 0.3*self.salary
exp1=employee(1,"AB",10)
exp2=employee(1,"CD",20)
print(exp1.get_tax())
print(exp2.get_tax())

