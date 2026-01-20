import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch

# Add the project root to the path to allow for relative imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import core components and patterns
from core.singleton.singleton import Singleton, ConfigManager
from core.controller import SmartCityController, get_controller
from core.factories.factory_method import SmartCityComponent, ComponentFactory
from core.builders.report_builder import ReportDirector, EnergyReportBuilder
from core.proxy.proxy import SubsystemProxy, RealSubsystem

# Import subsystem components for testing
from modules.transport.manager import TrafficLight, TrafficLightFactory
from modules.energy.manager import EnergyManager
from modules.security.manager import SecurityManager

class TestDesignPatterns(unittest.TestCase):

    def test_01_singleton_pattern(self):
        """Test the Singleton pattern implementation."""
        # Test ConfigManager (metaclass=Singleton)
        manager1 = ConfigManager()
        manager2 = ConfigManager()
        self.assertIs(manager1, manager2, "Singleton instances should be the same object.")
        self.assertEqual(manager1.get_setting("log_level"), "INFO")

        # Test SmartCityController (metaclass=Singleton)
        controller1 = get_controller()
        controller2 = get_controller()
        self.assertIs(controller1, controller2, "SmartCityController should be a Singleton.")

    def test_02_factory_method_pattern(self):
        """Test the Factory Method pattern implementation."""
        factory = TrafficLightFactory(next_id=10)
        light1 = factory.create_component()
        light2 = factory.create_component()

        self.assertIsInstance(light1, TrafficLight)
        self.assertIsInstance(light2, TrafficLight)
        self.assertEqual(light1.light_id, 10)
        self.assertEqual(light2.light_id, 11)
        self.assertEqual(light1.state, "Red")
        self.assertEqual(light1.operate(), "TrafficLight 10 changed to Green")
        self.assertEqual(light1.state, "Green")

    def test_03_builder_pattern(self):
        """Test the Builder pattern implementation."""
        builder = EnergyReportBuilder()
        director = ReportDirector(builder)
        
        director.build_full_report()
        report = builder.get_result()
        
        self.assertIn("--- Energy Consumption Report ---", report.show())
        self.assertIn("Total Consumption (kWh):", report.show())
        self.assertIn("--- End of Report ---", report.show())

    def test_04_proxy_pattern(self):
        """Test the Proxy pattern implementation."""
        real_subsystem = RealSubsystem()
        proxy = SubsystemProxy(real_subsystem)

        # Test admin access (allowed)
        result_admin = proxy.request("admin")
        self.assertIn("Real Subsystem: Executing request", result_admin)

        # Test guest access (denied)
        result_guest = proxy.request("guest")
        self.assertIn("Proxy: Access denied", result_guest)

    def test_05_facade_pattern(self):
        """Test the Facade pattern implementation via SmartCityController."""
        controller = get_controller()
        
        # Test get_all_status
        status = controller.get_all_status()
        self.assertIsInstance(status, dict)
        self.assertIn("transport", status)
        self.assertIn("lighting", status)
        self.assertIn("security", status)
        self.assertIn("energy", status)

        # Test run_simulation (high-level operation)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            sim_status = controller.run_simulation()
            self.assertIn("--- Running SmartCity Simulation Cycle ---", fake_out.getvalue())
            self.assertIn("--- Simulation Cycle Complete ---", fake_out.getvalue())
            self.assertIsInstance(sim_status, dict)

class TestSubsystems(unittest.TestCase):
    
    def setUp(self):
        # The controller is a singleton, so we just retrieve the instance
        self.controller = get_controller()

    def test_06_transport_subsystem(self):
        """Test Transport Subsystem operation."""
        result = self.controller.operate_subsystem("transport", "optimize_flow")
        self.assertIn("Transport: Optimized traffic flow.", result)
        status = self.controller.get_subsystem_status("transport")
        self.assertIn("Operational", status["manager_status"])
        self.assertEqual(len(status["components"]), 3)

    def test_07_security_subsystem(self):
        """Test Security Subsystem operation (Proxy in action)."""
        # Test 'run_patrol' which should use 'admin' role via proxy
        result = self.controller.operate_subsystem("security", "run_patrol")
        self.assertIn("Security System: Initiating full city patrol.", result)
        
        # Test a non-admin operation (default 'manager' role)
        result_basic = self.controller.operate_subsystem("security", "basic_query")
        self.assertIn("Access limited.", result_basic) # The SecurityManager uses 'manager' role for non-specific actions, which is limited by the proxy.

    def test_08_energy_subsystem(self):
        """Test Energy Subsystem operation (Builder in action)."""
        result = self.controller.operate_subsystem("energy", "report_consumption")
        self.assertIn("Energy: Generated Consumption Report:", result)
        self.assertIn("Total Consumption (kWh):", result)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
