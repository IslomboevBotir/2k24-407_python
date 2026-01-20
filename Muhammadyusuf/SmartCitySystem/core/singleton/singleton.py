class Singleton(type):
    """
    Design Pattern: Singleton (Creational)
    Purpose: Ensures a class has only one instance and provides a global point of access to it.
    Usage: Used for the central SmartCityController to manage the entire system.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# Example of a non-system class that might use Singleton
class ConfigManager(metaclass=Singleton):
    def __init__(self):
        self.settings = {"log_level": "INFO"}

    def get_setting(self, key):
        return self.settings.get(key)
