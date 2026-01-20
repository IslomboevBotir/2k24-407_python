from core.factories.factory_method import SmartCityComponent
import random

# --- Abstract Factory (Base) ---
class StreetLightFactory:
    """
    Design Pattern: Abstract Factory (Creational)
    Purpose: Provides an interface for creating families of related or dependent objects
             without specifying their concrete classes.
    Usage: Used to create different 'families' of street lights (e.g., LED vs. Halogen).
    """
    def create_light(self):
        pass

    def create_sensor(self):
        pass

# --- Concrete Products ---
class LEDLight(SmartCityComponent):
    def __init__(self, light_id):
        self.light_id = light_id
        self.brightness = 50

    def operate(self):
        self.brightness = random.randint(30, 100)
        return f"LED Light {self.light_id} adjusted to {self.brightness}%"

    def get_status(self):
        return f"LED Light {self.light_id}: {self.brightness}%"

class HalogenLight(SmartCityComponent):
    def __init__(self, light_id):
        self.light_id = light_id
        self.brightness = 70

    def operate(self):
        self.brightness = random.randint(50, 100)
        return f"Halogen Light {self.light_id} adjusted to {self.brightness}%"

    def get_status(self):
        return f"Halogen Light {self.light_id}: {self.brightness}%"

class MotionSensor:
    def detect(self):
        return random.choice([True, False])

# --- Concrete Factories ---
class EnergyEfficientFactory(StreetLightFactory):
    def __init__(self):
        self.light_id_counter = 1

    def create_light(self):
        light = LEDLight(self.light_id_counter)
        self.light_id_counter += 1
        return light

    def create_sensor(self):
        return MotionSensor()

# --- Subsystem Manager ---
class LightingManager:
    def __init__(self):
        self.factory = EnergyEfficientFactory()
        self.lights = [self.factory.create_light() for _ in range(5)]
        self.sensor = self.factory.create_sensor()
        self.status = "Operational"

    def operate(self, action=None):
        if action == "adjust_brightness":
            results = [c.operate() for c in self.lights]
            return f"Lighting: Adjusted brightness based on time/motion. Changes: {results}"
        return "Lighting: No specific action taken."

    def get_status(self):
        component_statuses = [c.get_status() for c in self.lights]
        return {"manager_status": self.status, "components": component_statuses, "sensor_active": self.sensor.detect()}
