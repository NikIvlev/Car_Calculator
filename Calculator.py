from apis import get_gas_price, get_power_price

class Calculator:
    def __init__(self,mileage=15000):
        self.mileage = mileage
        self.cars = {}          # Car: Year price


    def add_car(self, car):
        self.cars[car] = car.year_cost(self.mileage, )


class Car:
    def __init__(self,name:str,price:int,fuel_economy:float,service_cost:int,insurance_cost:int):
        self.name = name
        self.price = price
        self.fuel_economy = fuel_economy
        self.service_cost = service_cost
        self.insurance_cost = insurance_cost

    def static_year_cost(self):
        return self.service_cost + self.insurance_cost
    def dynamic_year_cost(self, mileage:int, fuel_price):
        return self.fuel_economy * mileage / 100 * fuel_price

    def year_cost(self, mileage:int, fuel_price: float):
        return self.static_year_cost + self.dynamic_year_cost(mileage, fuel_price)


class ElectricCar(Car):
    def __init__(self, name: str, price: int, fuel_economy:float, service_cost: int, insurance_cost: int, power_consumption:int):
        super().__init__(name=name, price=price, fuel_economy=0, service_cost=0, insurance_cost=insurance_cost)
        self.power_consumption = power_consumption #WT / 1km

    def dynamic_year_cost(self, mileage: int, kilowatt_price:float):
        return self.power_consumption * mileage / 1000 * kilowatt_price



