""" 
This is the header of the python file
company name: pythoncourse
"""

# Method overriding


class Person:

    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def __str__(self):  # will print the value by calling the instance of class
        return self.firstname + " " + self.lastname + ", " + str(self.age)

    def modify_age(self, amount):
        return self.age+amount


class Employee(Person):

    def __init__(self, first, last, age, staffnum):
        super().__init__(first, last, age)
        self.staffnumber = staffnum

    def __str__(self):
        return super().__str__() + ", " +  self.staffnumber

    def modify_age(self, amount):
        return super().modify_age(amount) * amount


x = Person("Marge", "Simpson", 36)
y = Employee("Homer", "Simpson", 28, "1007")

print(x)
print(y)
#print(x.modify_age(10))
#print(y.modify_age(2))