# multi level inheritance

class Food:

    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print(f'Name of the food {self.name}')
        print(f'Price : {self.price}')  

class Fastfood(Food):

    def __init__(self, name, price,res_name,order_type,pyment_type):
        super().__init__(name, price)
        self.res_name=res_name
        self.order_type=order_type
        self.pyment_type=pyment_type
    def show(self):
        super().display()    
        print(f'Resturent name :{self.res_name}')
        print(f'Order type :{self.order_type}')
        print(f'Pyment mode {self.pyment_type}')

class Pizza(Fastfood):

    def __init__(self, name, price, res_name, order_type, pyment_type,toping,size,adding_option):
        super().__init__(name, price, res_name, order_type, pyment_type)
        self.toping=toping
        self.size=size
        self.adding_option=adding_option
    def details(self):
        super().show()
        print(f'Toping {self.toping}')   
        print(f'size {self.size}')   
        print(f'Adding options {self.adding_option}')   
obj=Pizza('pizza',899,'baba the dhabha','online','cash','veg topping','8n inch','Add panner,extra chees')
obj.details()        
        
        