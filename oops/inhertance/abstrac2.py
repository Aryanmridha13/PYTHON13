from abc import ABC,abstractmethod

class Mobile(ABC):

    @abstractmethod
    def apps(self):
        pass

    @abstractmethod
    def locks(self):
        pass

    @abstractmethod
    def ois(self):
        pass

    @abstractmethod
    def oredr_con(self):
        pass

class Smartph(Mobile):

    def ois(self):
        print("Ois is android")

    def locks(self):
        print("Phone unlock")

    def apps(self):
        print("app is open")
    def oredr_con(self):
        print("Order Done")    

obj=Smartph()

obj.ois()
obj.locks()
obj.apps()
obj.oredr_con()
