from Vehicle.Vehicle import Vehicle


class Motorcycle(Vehicle):
    one_engine_power_value_to_one_kg = 10

    def __init__(self, make: str, model: str, year: int, weight: int, engine_power: int):

        one_engine_power_value_to_one_kg = -1

        if make == "Harley" and model == "Sportster":
            one_engine_power_value_to_one_kg = 12
        elif make == "Honda" and model == "CBR":
            one_engine_power_value_to_one_kg = 15
        else:
            # Default value if no specific conditions match
            one_engine_power_value_to_one_kg = 10

        super().__init__(make, model, year, weight, engine_power, one_engine_power_value_to_one_kg)

    def get_towing_capacity(self):
        return self.engine_power * self.one_engine_power_value_to_one_kg - self.weight
