class Employee:
    def __init__(self,name,emp_id,sal):
        self.name = name
        self.emp_id = emp_id
        self.sal = sal

    def disp(self):
        print("Name =", self.name)
        print("Employee ID =", self.emp_id)
        print("Salary =", self.sal)

class Employee_2:
    @staticmethod
    def display(e):
        e.disp()

n1 = input("Enter you name = ")
e1 = Employee(n1, 12345, 2000000)
Employee_2.display(e1)