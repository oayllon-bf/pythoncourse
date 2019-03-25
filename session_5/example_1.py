""" 
This is the header of the python file
company name: pythoncourse
"""

# single inheritance

class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def name(self):
        return self.firstname + " " + self.lastname


class Employee(Person):
    def __init__(self, first, last, staffnum):
        Person.__init__(self, first, last)
        #super().__init__(first, last)
        #super(Employee, self).__init__(first, last)
        self.staffnumber = staffnum

    def get_employee(self):
        return self.name() + ", " + self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.name())
print(y.get_employee())
