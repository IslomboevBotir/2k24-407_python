from abc import ABC, abstractmethod

# --- Abstract Component ---
class SmartCityComponent(ABC):
    """
    Abstract base class for all SmartCity components (lights, vehicles, sensors, etc.).
    """
    @abstractmethod
    def operate(self):
        pass

    @abstractmethod
    def get_status(self):
        pass

# --- Abstract Factory Method ---
class ComponentFactory(ABC):
    """
    Design Pattern: Factory Method (Creational)
    Purpose: Defines an interface for creating an object, but lets subclasses alter the type of objects that will be created.
    Usage: Used by subsystems to create different types of components (e.g., a TrafficLightFactory creates TrafficLights).
    """
    @abstractmethod
    def create_component(self) -> SmartCityComponent:
        """The Factory Method declaration."""
        pass
