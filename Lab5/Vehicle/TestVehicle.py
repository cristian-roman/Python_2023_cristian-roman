from Vehicle.Car import Car
from Vehicle.Motorcycle import Motorcycle
from Vehicle.Truck import Truck

class TestVehicle:

    @staticmethod
    def test_vehicles():
        for vehicle in [Car("Toyota", "Camry", 2018, 2000, 150), Truck("Ford", "F-150", 2019, 4000, 220), Motorcycle("Honda", "CBR", 2018, 500, 100)]:
            print(f"\"{vehicle.make} {vehicle.model}\"")
            print(f"Year: {vehicle.year}")
            print(f"Weight: {vehicle.weight}")
            print(f"Engine Power: {vehicle.engine_power}")
            print(f"Horse Power to KG: {vehicle.horse_power_to_kg}")
            print(f"Towing Capacity: {vehicle.get_towing_capacity()}")
            print()