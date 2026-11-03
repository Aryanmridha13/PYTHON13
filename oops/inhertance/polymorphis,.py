class Animal:
    name = 'Animal'
    def speak(self):
        print("animal speak")
class Dog(Animal):

    def speak(self):
        print("Dog speak vow")   

class Lion(Animal):
    def speak(self):
        print("loin spek tryy")

obj=Dog() 
obj.speak()

obj1=Lion()
obj1.speak()
obj1.speak()
obj1.speak()
obj1.speak()