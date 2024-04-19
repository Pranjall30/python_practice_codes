class student:
    exams_given=[]
    def __init__(self,id):
        self.id=id
        self.college="AB"
st1=student(5)
st2=student(7)
st1.exams_given.append("JEE")
st2.exams_given.append("NEET")
print(st1.id)
print(st2.id)
print(st1.exams_given)
print(st2.exams_given)
print(st1.college)