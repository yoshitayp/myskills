class Father:
    def skills(self):
        print("Father:Driving")
        class Mother:
            def skills(self):
                print("Mother:Cooking")
                class Child(Father,Mother):
                    def skills(self):
                        print("Child:Playing")
                        
                        obj=Child()
                        obj.skills()