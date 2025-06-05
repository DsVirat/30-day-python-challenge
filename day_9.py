class Car:
    def __init__(self,brand,model,year,mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
       

    def display(self):
        print(f"This is {self.brand} {self.model} launched in {self.year} with a mileage of {self.mileage}km/L.\n{self.model} is a fuel car")

    def start(self):
        print(f"The {self.model}'s engine is starting")
    
class ElectricCar(Car):
    def __init__(self, brand, model, year, range):
        # calls parent constructor with brand, model, year, mileage=0
        # Initialize parent class with a default mileage value of 0, since electric cars don't use km/L
        super().__init__(brand, model, year, mileage=0) 
        self.range = range
    
    def display(self):
        print(f"This is {self.brand} {self.model} launched in {self.year} with a range of {self.range}Km/KwH.\n{self.model} is an electric car")


c = Car("Maruti Suzuki","Brezza","2020",16)
c.display()
c.start()

e = ElectricCar("Tata","Nexon Hybrid","2024",500)
e.display()
e.start()