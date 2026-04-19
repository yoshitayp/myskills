class Parent:
    def show(self):
        print("This is Parent class")
class Child(Parent):
    def display(self):
        print("This is Chlid class")
        obj=Child()
        obj.show()
        obj.display()