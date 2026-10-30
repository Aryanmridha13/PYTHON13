from abc import ABC,abstractmethod
class Fan(ABC):
    min_speed = 1
    max_speed=5

    def __init__(self,current_speed,blead):
        self.cureent_speed = current_speed
        self.blead=blead

    def motor(self):
        print("Motor is rotating")

    @abstractmethod
    def trun_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def speed(self):
        pass


class Celling_fan(Fan):

    def trun_on(self):
        print("Fan in On")        

    def turn_off(self):
                print("Fan in Off")  
    def speed(self):
         print(f"speed is {self.cureent_speed}")              


obj=Celling_fan(3,4)
obj.trun_on()
obj.motor()
obj.speed()
obj.turn_off()


