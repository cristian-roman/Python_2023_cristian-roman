class Vehicle:
    def __init__(self, make: str, model: str, year: int, weight: int, engine_power: int, horse_power_to_kg: int):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.engine_power = engine_power
        self.horse_power_to_kg = horse_power_to_kg

    def get_towing_capacity(self):
        raise NotImplementedError
