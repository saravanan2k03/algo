class Employee():
    def __init__(self,aname,asalary):
        self.name =aname
        self.salary =asalary

    def printname(self):
        return f"{self.name}, {self.salary}"
    

saro = Employee('saro',100)

saro.name='John'
saro.salary=100

print(saro.printname())