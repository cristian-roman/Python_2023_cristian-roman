import random

from Vehicle.Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, weight: int, engine_power: int):
        horse_power_to_kg = -1
        if make == "Toyota" and model == "Camry":
            horse_power_to_kg = 150
        elif make == "Ford" and model == "Mustang":
            horse_power_to_kg = 180
        else:
            # Default value if no specific conditions match
            horse_power_to_kg = 130

        super().__init__(make, model, year, weight, engine_power, horse_power_to_kg)

    def get_towing_capacity(self):
        return self.engine_power * self.horse_power_to_kg - self.weight
