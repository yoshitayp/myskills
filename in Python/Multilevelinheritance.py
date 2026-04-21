class Grandparent:
    def show(self):
        print("this is grandparent class")
        Class Parent(Grandparent)
        def show(self):
            print("this is parent class")
            class Child(Parent):  
                def show(self):
                    print("this is child class")

                    obj=Child()
                    obj.show()
                    obj.display()
                    obj.info()