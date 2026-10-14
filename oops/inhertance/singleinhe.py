# # Single level inhertance 

# class Animal :

#     def __init__(self,name):
#         self.name= name
#     def display(self):
#         print("It is a Animal class")    

# class Dog(Animal):
#     def __init__(self, name, type , bread):
#         super().__init__(name)
#         self.type=type
#         self.bread=bread
#     def display(self):
         
#          print('it is a Dog class ')
#          print(f'name :{self.name}')
#          print(f'name :{self.type}')
#          print(f'name :{self.bread}')

#          super().display()    

# obj=Dog('sheru','dog','german')
# obj.display()      

# ! School and Teacher

class School:
    sname='Bhopal School'   
    sch_code=123456
    def __init__(self,name):
        self.name=name

    def details(self):
        print("school Details\nit is a primary school\n 1 to 5th ")

class Teacher(School):
    def __init__(self,name,subject,Class):
        super().__init__(name)
        self.subject=subject
        self.Class=Class
    def details(self):
        print(f'name is {self.name}')    
        print(f'Scool name is {School.sname}')
        print(f'Scool code is {School.sch_code}')
        print(f'subject is {self.subject}')    
        print(f'Teaching class is {self.Class}')  

        # super().details()
class Student(Teacher):
    def __init__(self, name, subject, Class,numers,montor):
        super().__init__(name, subject, Class)    
        self.number=numers
        self.montor=montor

    def data(self):
        super().details()
        print(f'student number {self.number}')
        print(f'Mentor of the classs {self.montor}')   

        School.details(self) 


# obj=Teacher('Aryan','copmuter','5th' )
# obj.details()

obj=Student('Aryan','Computer',"5th",'25','harsh')
obj.data()
        
             