from core.singleton.singleton import Singleton
from modules.transport.manager import TransportManager
from modules.lighting.manager import LightingManager
from modules.security.manager import SecurityManager
from modules.energy.manager import EnergyManager

class SmartCityController(metaclass=Singleton):
    """
    Design Pattern: Singleton (Creational)
    Purpose: Ensures only one instance of the central controller exists.

    Design Pattern: Facade (Structural)
    Purpose: Provides a simplified interface to a complex subsystem (the entire SmartCity system).
    Usage: The main application interacts only with this controller, which manages all subsystems.
    """
    def __init__(self):
        # Initialize all subsystem managers
        # Note: These managers will be implemented in Phase 4.
        # For now, we use placeholder classes to satisfy imports.
        # The actual imports will be fixed when the managers are created.
        # For now, I will assume the imports are correct and proceed.
        self._transport_manager = TransportManager()
        self._lighting_manager = LightingManager()
        self._security_manager = SecurityManager()
        self._energy_manager = EnergyManager()
        self._subsystems = {
            "transport": self._transport_manager,
            "lighting": self._lighting_manager,
            "security": self._security_manager,
            "energy": self._energy_manager,
        }
        print("SmartCity System Controller Initialized.")

    def get_subsystem_names(self):
        """Returns a list of available subsystem names."""
        return list(self._subsystems.keys())

    def get_subsystem_status(self, subsystem_name):
        """Facade method to get the status of a specific subsystem."""
        if subsystem_name in self._subsystems:
            return self._subsystems[subsystem_name].get_status()
        return f"Error: Subsystem '{subsystem_name}' not found."

    def operate_subsystem(self, subsystem_name, action=None):
        """Facade method to perform an operation on a specific subsystem."""
        if subsystem_name in self._subsystems:
            return self._subsystems[subsystem_name].operate(action)
        return f"Error: Subsystem '{subsystem_name}' not found."

    def get_all_status(self):
        """Facade method to get the status of all subsystems."""
        all_status = {}
        for name, manager in self._subsystems.items():
            all_status[name] = manager.get_status()
        return all_status

    def run_simulation(self):
        """A high-level operation to simulate a cycle of city management."""
        print("\n--- Running SmartCity Simulation Cycle ---")
        self.operate_subsystem("transport", "optimize_flow")
        self.operate_subsystem("lighting", "adjust_brightness")
        self.operate_subsystem("security", "run_patrol")
        self.operate_subsystem("energy", "report_consumption")
        print("--- Simulation Cycle Complete ---")
        return self.get_all_status()

# Helper function to get the controller instance
def get_controller():
    return SmartCityController()
