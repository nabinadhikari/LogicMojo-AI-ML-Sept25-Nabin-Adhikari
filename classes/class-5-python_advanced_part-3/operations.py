class Person:
    def __init__(self, name):
        self.name = name
    def describe(self):
        print(f'Person {self.name}')


class Employee(Person):
    def __init__(self, name, company):
        self.company = company
        self.name = name
        super().__init__(name)
    def describe(self):
        print(f'Employee {self.name} from {self.company}')