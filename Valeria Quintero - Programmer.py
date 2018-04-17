class Person(object):
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def work(self):
        print("%s goes to work" % self.name)

class Employee(Person):
    def __init__(self, name, age, job):
        super(Employee, self).__init__(name, age, job)

    def drive(self):
        print("%s drives to work" % self.name)

    def run(self):
        print("%s runs to work because he is late" % self.name)

class Programmer(Employee):
    def __init__(self, name, job, age):
        super(Programmer, self).__init__(name, age, job)

    def work(self):
        print("He works at %s" % self.job)

    def age(self):
        print("He is %d years old" % self.age)

the_Person = Person("Bob", "18", "Target")
the_Employee = Person("Bob", "18", "Target")
the_Programmer = Employee("Bob", "18", "Target")
