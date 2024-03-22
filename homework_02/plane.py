"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self,
                 weight: int = 0,
                 fuel: int = 0,
                 fuel_consumption: int = 1,
                 max_cargo: int = 1):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = self.check_max_cargo(max_cargo)

    @staticmethod
    def check_max_cargo(max_cargo):
        if max_cargo <= 0:
            raise ValueError()
        else:
            return max_cargo

    def load_cargo(self, cargo: int) -> None:
        if cargo + self.cargo <= self.max_cargo:
            self.cargo += cargo
        else:
            raise CargoOverload(f'Cargo overload for plane!')

    def remove_all_cargo(self):
        res = self.cargo
        self.cargo = 0
        return res
