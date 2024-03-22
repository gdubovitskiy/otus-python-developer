from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel, DistanceNegativeError, NegativeFuelConsumption


class Vehicle(ABC):
    def __init__(self, weight: int = 0, fuel: int = 0, fuel_consumption: int = 1):
        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = self.check_fuel_consumption(fuel_consumption)

    @staticmethod
    def check_fuel_consumption(fuel_consumption: int) -> int:
        if fuel_consumption < 0:
            raise NegativeFuelConsumption('Fuel consumption cannot be less than 0!')
        else:
            return fuel_consumption

    def start(self):
        if not self.started and self.fuel > 0:
            self.started = True
        elif self.started:
            print('You\'re already started!')
        else:
            raise LowFuelError('Fuel is empty!')

    def move(self, distance: int):
        if distance >= 0:
            if self.fuel >= self.fuel_consumption * distance:
                self.fuel -= self.fuel_consumption * distance
            else:
                raise NotEnoughFuel('Not enough fuel!')
        else:
            raise DistanceNegativeError('Distance value is negative!')
