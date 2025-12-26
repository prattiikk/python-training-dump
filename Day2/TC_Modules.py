def welcome():
    print("Welcome to mymodule")


data = "This is module data"


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("Stuent Name:",self.name)
        print("Stuent age:", self.age)