#/usr/bin/env python3 
"""
title: classes_method_types.py
author: exm5840
date(created): 2019-09-19 19:05:11 EDT
date (updated): 2019-09-19 19:05:11 EDT
"""

class Employee:
    """
    Creates the info for an Employee
    """
    emp_count = 0

    def __init__(self, name, ldap):
        self.name = name
        self.ldap = ldap
        Employee.emp_count += 1


## Takes one parameter, self, which points to an instance of the class when the method is called.
## Can freely access attributes and other methods on the same object.
## Able to modify an object’s class’s state.
## Can access the class itself through the self.class attribute.
    def display_employee(self):
        print (f"Name: {self.name}, LDAP: {self.ldap}")


## Marked with a @classmethod decorator to flag it as a class method.
## Take a cls parameter that points to the class—and not the object instance—when the method is called.
## It can’t modify object instance state. (That would require access to self.)
## It can still modify class state.
    @classmethod
    def get_count(cls):
        return Employee.emp_count


## Marked with a @staticmethod decorator to flag it as a static method.
## Takes neither a self nor a cls parameter (but free to accept other parameters).
## It can neither modify object state nor class state.
## Static methods are restricted in what data they can access.
    @staticmethod
    def take_home_salary(salary):
        return salary * 0.7

if __name__ == "__main__":
        print("=================================")
    e1 = Employee("Hellen", 25000)
    e1.display_employee()
    print(f"Number of Employees: {Employee.get_count()}")
    print(f"Potential Salary: {Employee.take_home_salary(100)}")

    print("=================================")
    e2 = Employee("Jackson", 58000)
    e2.display_employee()
    print(f"Number of Employees: {Employee.get_count()}")
    print(f"Potential Salary: {Employee.take_home_salary(350)}")
## Instance methods need a class instance and can access the instance through self.
## Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.
## Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.
