class person:
    def __init__(self,name):
        self.name = name
        # child class
class student(person):
    def __init__(self, name):
        super().__init__(name)
        self.subjects =[]
        self.marks =[]
        # total marks calculation method 
    def calculate_total(self):
        return sum(self.marks)
    # average marks calculation
    def calculate_average(self):
       return sum(self.marks)/len(self.marks)
#    grade calculation
    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 85:
          return "A"
        elif avg >= 70:
           return "B"
        elif avg >=60:
            return "C"
        else:
             return "F"
name = input("enter your name:")
s = student(name)
n = int(input("how many subjects ?:"))
for i in range(n):
    subject = input("enter your subject:")
    marks = int (input("enter your marks:"))
    s.subjects.append(subject)
    s.marks.append(marks)
print("-------------report card-----------")
print("name:", name)
for i in range(len(s.subjects)):
    print(s.subjects[i], ":", s.marks[i])
# method calling
print("Total:", s.calculate_total())
print("Average:", s.calculate_average())
print("Grade:", s.calculate_grade())


        
        
        