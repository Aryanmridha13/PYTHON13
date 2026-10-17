# Hierarchical inheritance: multiple child classes inherit from one parent.

# Real-time example: different employees in a company share basic employee details.
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def show_details(self):
        print(f"Employee Name : {self.name}")
        print(f"Employee ID   : {self.employee_id}")


class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size

    def manage_team(self):
        print(f"{self.name} manages a team of {self.team_size} employees.")


class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language

    def write_code(self):
        print(f"{self.name} develops software using {self.programming_language}.")


class Designer(Employee):
    def __init__(self, name, employee_id, design_tool):
        super().__init__(name, employee_id)
        self.design_tool = design_tool

    def create_designs(self):
        print(f"{self.name} creates designs using {self.design_tool}.")


manager = Manager("Asha", 101, 6)
developer = Developer("Ravi", 102, "Python")
designer = Designer("Mina", 103, "Figma")

print("===== Manager =====")
manager.show_details()
manager.manage_team()

print("\n===== Developer =====")
developer.show_details()
developer.write_code()

print("\n===== Designer =====")
designer.show_details()
designer.create_designs()
