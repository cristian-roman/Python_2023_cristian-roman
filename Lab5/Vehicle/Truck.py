from Vehicle.Vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, make: str, model: str, year: int, weight: int, engine_power: int):
        horse_power_to_kg = -1
        if make == "Chevrolet" and model == "Silverado":
            horse_power_to_kg = 200
        elif make == "Ford" and model == "F-150":
            horse_power_to_kg = 220
        else:
            # Default value if no specific conditions match
            horse_power_to_kg = 180

        super().__init__(make, model, year, weight, engine_power, horse_power_to_kg)

    def get_towing_capacity(self):
        # Assuming a simple formula for towing capacity based on payload and engine power
        return self.engine_power * self.horse_power_to_kg - self.weight
