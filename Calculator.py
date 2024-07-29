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

    def static_year_cost(self):
        return self.service_cost + self.insurance_cost
    def dynamic_year_cost(self, mileage:int):
        return self.fuel_economy * mileage / 100 * fuel_price

    def year_cost(self, mileage:int, fuel_price: float):
        return self.static_year_cost + self.dynamic_year_cost(mileage, fuel_price)


class ElectricCar(Car):
    def __init__(self, name: str, price: int, service_cost: int, insurance_cost: int, power_consumption:int):
        super().__init__(name, price, 0, service_cost, insurance_cost)
        self.power_consumption = power_consumption #WT / 1km



