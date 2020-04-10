# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# =============== Vehicles ===============
class Vehicle:
    def __init__(self):
        pass


# =============== Flight Vehicles ===============
class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass


class StartShip(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass


class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass


# =============== Ground Vehicles ===============
class GroundVehicles(Vehicle):
    def __init__(self):
        super().__init__()
        pass


class Car(GroundVehicles):
    def __init__(self):
        super().__init__()
        pass


class Motorcycle(GroundVehicles):
    def __init__(self):
        super().__init__()
        pass
