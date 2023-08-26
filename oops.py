class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary
    

sudarshan = Employee("Sudarshan", "40000")
print(sudarshan.name)
print(sudarshan.salary)   
print(sudarshan.getSalary()) 