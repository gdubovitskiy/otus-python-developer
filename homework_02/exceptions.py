"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    pass

class NotEnoughFuel(Exception):
    pass

class CargoOverload(Exception):
    pass

class DistanceNegativeError(Exception):
    pass

class NegativeFuelConsumption(Exception):
    pass