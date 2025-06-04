# Define a class called "car"
class Car:

    # method to initialize class attributes
    def __init__(self, brand, model, price, year):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year

    # method to display car's info
    def display(self):
        print(f'Brand Name : {self.brand} \nModel Name: {self.model} \nBought in : {self.year} \nPrice : {self.price} ')

# creating instances of the class car
car_1 = Car("Maruti Suzuki","Brezza",958400,"2019")
car_2 = Car("Tata","Nexon",828600,"2022")

# Calling display method to show car's info   
car_1.display()
car_2.display()