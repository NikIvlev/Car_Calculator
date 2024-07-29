import Calculator


if __name__ == '__main__':
    calc = Calculator.Calculator
    calc.add_car(
        Calculator.Car("Toyota Corolla", 30000, 7, 1200, 2500)
    )
    calc.add_car(
        Calculator.ElectricCar("Tesla Model 3", 200000, 55000, 150)
    )
    calc.add_car(
        Calculator.Car("Range Rover", 650000, 3, 3000, 7000)
    )

calc.print.cars()
