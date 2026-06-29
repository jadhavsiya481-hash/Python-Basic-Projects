class Employee:
    def __init__(self, i, n, d, s):
        self.id = i 
        self.name = n
        self.details = (d,s)

    def show_details(self):
        print(self.id, self.name, self.details)

e = {}

for i in range(3):
    x = Employee(input("ID:"), input("Name:"), input("Dept:"), input("Salary:"))
    e[x.id] = x

for i in e.values():
    i.show_details()       