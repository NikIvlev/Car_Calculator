class Calculator:
    def __init__(self):
        self.cars = []

class Car:
    def __init__(self,name:str,price:int,fuel_economy:float,service_cost:int,insurance_cost:int):
        self.name = name
        self.price = price
        self.fuel_economy = fuel_economy
        self.service_cost = service_cost
        self.insurance_cost = insurance_cost
