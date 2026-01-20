from core.factories.factory_method import SmartCityComponent, ComponentFactory
import random

# --- Concrete Components ---
class TrafficLight(SmartCityComponent):
    def __init__(self, light_id):
        self.light_id = light_id
        self.state = "Red"

    def operate(self):
        if self.state == "Red":
            self.state = "Green"
        elif self.state == "Green":
            self.state = "Yellow"
        elif self.state == "Yellow":
            self.state = "Red"
        return f"TrafficLight {self.light_id} changed to {self.state}"

    def get_status(self):
        return f"Light {self.light_id}: {self.state}"

# --- Concrete Factory ---
class TrafficLightFactory(ComponentFactory):
    def __init__(self, next_id):
        self.next_id = next_id

    def create_component(self) -> SmartCityComponent:
        light = TrafficLight(self.next_id)
        self.next_id += 1
        return light

# --- Subsystem Manager ---
class TransportManager:
    def __init__(self):
        self.factory = TrafficLightFactory(next_id=1)
        self.components = [self.factory.create_component() for _ in range(3)]
        self.status = "Operational"

    def operate(self, action=None):
        if action == "optimize_flow":
            results = [c.operate() for c in self.components]
            return f"Transport: Optimized traffic flow. Changes: {results}"
        return "Transport: No specific action taken."

    def get_status(self):
        component_statuses = [c.get_status() for c in self.components]
        return {"manager_status": self.status, "components": component_statuses}
