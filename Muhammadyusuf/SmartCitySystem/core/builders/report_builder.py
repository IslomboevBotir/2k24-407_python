from abc import ABC, abstractmethod

class SmartCityReport:
    """The complex object to be constructed."""
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def show(self):
        return "\n".join(self.parts)

class ReportBuilder(ABC):
    """
    Design Pattern: Builder (Creational)
    Purpose: Separates the construction of a complex object from its representation,
             allowing the same construction process to create different representations.
    Usage: Used to construct complex reports (e.g., Energy Consumption Report) step-by-step.
    """
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_header(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_footer(self):
        pass

    @abstractmethod
    def get_result(self) -> SmartCityReport:
        pass

class ReportDirector:
    """
    The Director class manages the construction process.
    """
    def __init__(self, builder: ReportBuilder):
        self._builder = builder

    @property
    def builder(self) -> ReportBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: ReportBuilder):
        self._builder = builder

    def build_full_report(self):
        """A standard construction process."""
        self.builder.reset()
        self.builder.build_header()
        self.builder.build_body()
        self.builder.build_footer()
