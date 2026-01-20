from abc import ABC, abstractmethod

class SubsystemInterface(ABC):
    """
    The Subject interface, common to both the RealSubject and the Proxy.
    """
    @abstractmethod
    def request(self, user_role: str):
        pass

class RealSubsystem(SubsystemInterface):
    """
    The RealSubject, containing the core business logic.
    """
    def request(self, user_role: str):
        return f"Real Subsystem: Executing request for user with role '{user_role}'."

class SubsystemProxy(SubsystemInterface):
    """
    Design Pattern: Proxy (Structural)
    Purpose: Provides a surrogate or placeholder for another object to control access to it.
    Usage: Used to control access to the Security Subsystem based on user roles (e.g., only 'admin' can access certain features).
    """
    def __init__(self, real_subsystem: RealSubsystem):
        self._real_subsystem = real_subsystem
        self._allowed_roles = ["admin", "manager"]

    def request(self, user_role: str):
        if self._check_access(user_role):
            return self._real_subsystem.request(user_role)
        else:
            return f"Proxy: Access denied for user role '{user_role}'. Must be one of {self._allowed_roles}."

    def _check_access(self, user_role: str) -> bool:
        print(f"Proxy: Checking access for role '{user_role}'...")
        return user_role in self._allowed_roles
