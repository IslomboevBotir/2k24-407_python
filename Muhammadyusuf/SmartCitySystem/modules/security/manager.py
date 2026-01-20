from core.proxy.proxy import SubsystemInterface
import random

# --- Real Subject ---
class RealSecuritySystem(SubsystemInterface):
    """
    The actual security system that performs sensitive operations.
    """
    def __init__(self):
        self.patrol_status = "Idle"

    def request(self, user_role: str):
        if user_role == "admin":
            self.patrol_status = "Patrol in Progress"
            return f"Security System: Initiating full city patrol. Status: {self.patrol_status}"
        return f"Security System: Accessing basic monitoring data for role '{user_role}'."

    def get_status(self):
        return f"Patrol Status: {self.patrol_status}. Incidents: {random.randint(0, 2)}"

# --- Proxy ---
class SecuritySystemProxy(SubsystemInterface):
    """
    Design Pattern: Proxy (Structural)
    Purpose: Controls access to the RealSecuritySystem.
    Usage: Only 'admin' users can initiate a full city patrol.
    """
    def __init__(self, real_subsystem: RealSecuritySystem):
        self._real_subsystem = real_subsystem
        self._admin_roles = ["admin"]

    def request(self, user_role: str):
        if user_role in self._admin_roles:
            # Admin can perform the sensitive operation
            return self._real_subsystem.request(user_role)
        else:
            # Other roles get limited access
            return f"Proxy: Access limited. Only 'admin' can initiate patrol. Current status: {self._real_subsystem.get_status()}"

    def get_status(self):
        # Status check is not a sensitive operation, so it's passed through
        return self._real_subsystem.get_status()

# --- Subsystem Manager ---
class SecurityManager:
    def __init__(self):
        self._real_system = RealSecuritySystem()
        # The manager holds the proxy instance
        self.system_proxy = SecuritySystemProxy(self._real_system)
        self.status = "Monitoring"

    def operate(self, action=None):
        # Simulate a user role for the operation
        user_role = "manager" # Default role for routine operations
        if action == "run_patrol":
            user_role = "admin" # Only admin can run patrol via the proxy
        
        result = self.system_proxy.request(user_role)
        return f"Security: Operation '{action}' attempted with role '{user_role}'. Result: {result}"

    def get_status(self):
        return {"manager_status": self.status, "system_status": self.system_proxy.get_status()}
