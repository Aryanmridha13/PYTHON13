class Student:
    # class variable (shared by all instances)
    school = "ABC School"

    def __init__(self, name, roll_no, age, grade):
        # instance variables (unique to each object)
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Name    : {self.name}")
        
        print(f"Roll No : {self.roll_no}")
        print(f"Age     : {self.age}")
        print(f"Grade   : {self.grade}")
        print(f"School  : {self.school}")


# creating objects (instances) of the Student class
s1 = Student("Rahul", 101, 20, "A")
s2 = Student("Priya", 102, 21, "B")

print("--- Student 1 ---")
s1.display()

print("\n--- Student 2 ---")
s2.display()

