class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.marks = []
    def add_mark(self,mark):
        try:
            self.marks.append(float(mark))
        except ValueError:
            print("Invalid mark")
    def get_average(self):
        return sum(self.marks)/len(self.marks) 
    def display_info(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Marks:", self.marks)
        print("Average:", self.get_average())

s = Student(input("Name:"), input("Roll:"))
for i in range(3):
    s.add_mark(input(f"Mark{i+1}:"))
s.display_info()                          