from core.builders.report_builder import ReportBuilder, ReportDirector, SmartCityReport
import random

# --- Concrete Builder ---
class EnergyReportBuilder(ReportBuilder):
    """
    A concrete builder for creating an Energy Consumption Report.
    """
    def __init__(self):
        self.report = None
        self.reset()

    def reset(self):
        self.report = SmartCityReport()

    def build_header(self):
        self.report.add_part("--- Energy Consumption Report ---")
        self.report.add_part(f"Date: {random.choice(['2025-12-01', '2025-12-02'])}")

    def build_body(self):
        consumption = random.randint(1000, 5000)
        self.report.add_part(f"Total Consumption (kWh): {consumption}")
        self.report.add_part(f"Lighting Usage: {int(consumption * 0.3)} kWh")
        self.report.add_part(f"Transport Usage: {int(consumption * 0.4)} kWh")
        self.report.add_part(f"Security Usage: {int(consumption * 0.1)} kWh")
        self.report.add_part(f"Other Usage: {int(consumption * 0.2)} kWh")

    def build_footer(self):
        self.report.add_part("--- End of Report ---")

    def get_result(self) -> SmartCityReport:
        report = self.report
        self.reset()
        return report

# --- Subsystem Manager ---
class EnergyManager:
    def __init__(self):
        self.builder = EnergyReportBuilder()
        self.director = ReportDirector(self.builder)
        self.status = "Monitoring"

    def operate(self, action=None):
        if action == "report_consumption":
            self.director.build_full_report()
            report = self.builder.get_result()
            return f"Energy: Generated Consumption Report:\n{report.show()}"
        return "Energy: No specific action taken."

    def get_status(self):
        return {"manager_status": self.status, "current_consumption": random.randint(1000, 5000)}
