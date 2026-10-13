# Car calss encapsulation

# class Vhical:

#     delier = 'global dller'
#     def __init__(self,brand,name,color,engine,tyare):
#         self.brand=brand
#         self.name=name
#         self.color=color
#         self.engine=engine
#         self.tyare=tyare

#     def details(self):
#         print(f'Brand is {self.brand}')    
#         print(f'name of the vhical  is : {self.name}')    
#         print(f'Color of the vhical  is {self.color}')    
#         print(f'Brand is {self.brand}')    
#         print(f'Engine is {self.engine}')    
#         print(f'Tyares are {self.tyare}')    

# # v1=Vhical('Tata',"car",'red',"12Horse",4)
# # v1.details()
# print()


class Collage:
    collage_name = 'TIT'
    code='460220'

    def collage_info(self):
        print("TIT is one of the most popular collage in bhopal\nit provides many courses\nBTech \t Pharmacy \t BBA ")

class Student(Collage):

    def __init__(self,name,course,sem,year):
        self.name=name
        self.course=course
        self.sem=sem
        self.year=year

    def data(self):
        print('\n \t Student Details \n')
        print(f'Name is :{self.name}')
        print(f'Collage name is :{self.collage_name}')
        print(f'Course is : {self.course}')  
        print(f'Collage code is : {self.code}') 
        print(f'Sem is : {self.sem}')   
        print(f'Year is : {self.year}')  

        print("\n \tCollage Details \n") 
        self.collage_info()

student1=Student("Aryan","B.TECH",8,4)
student1.data()
            