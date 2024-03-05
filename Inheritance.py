class Employee:
    def __init__(self,name,emp_id,sal):
        self.name = name
        self.emp_id = emp_id
        self.sal = sal

    def disp(self, add):
        self.add = add
        print("Name =", self.name)
        print("Employee ID =", self.emp_id)
        print("Salary =", self.sal)

class Employee_2(Employee):
    def display(self):
        Employee.disp(self, "BLR")
        print("Address =", self.add)

e1 = Employee_2("Daniel", 12345, 200000)
e1.display()
