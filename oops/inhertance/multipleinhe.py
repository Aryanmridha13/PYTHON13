# Multiple Inheritance - A child class inherits from MORE THAN ONE parent class

# Real-time Example: A Child inherits qualities from both Father and Mother

class Father:
    def __init__(self):
        self.father_name = "Rajesh"

    def skills(self):
        print("Father's Skill : Playing Cricket")

    def eye_color(self):
        print("Eye Color from Father : Brown")


class Mother:
    def __init__(self):
        self.mother_name = "Sunita"

    def talents(self):
        print("Mother's Talent : Cooking & Painting")

    def hair_type(self):
        print("Hair Type from Mother : Curly")


# Child inherits from BOTH Father and Mother
class Child(Father, Mother):
    def __init__(self):
        # call both parent constructors
        Father.__init__(self)
        Mother.__init__(self)
        self.child_name = "Aman"

    def show_info(self):
        print(f"Child Name   : {self.child_name}")
        print(f"Father Name  : {self.father_name}")
        print(f"Mother Name  : {self.mother_name}")


# --- Creating object ---
c = Child()

print("===== Child's Info =====")
c.show_info()

print("\n===== Inherited from Father =====")
c.skills()
c.eye_color()

print("\n===== Inherited from Mother =====")
c.talents()
c.hair_type()

print("\n===== MRO (Method Resolution Order) =====")
print(Child.mro())
