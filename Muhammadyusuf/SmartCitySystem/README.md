# SmartCity System

## Project: SmartCity System

**Assignment Description:**
SmartCity System is a console application that simulates the operation of an intelligent city management system. The system combines various subsystems responsible for lighting, transportation, security, energy saving, monitoring, and other urban infrastructure functions. Each subsystem is implemented using design patterns that ensure architectural stability and extensibility of the project.

**Implementation Details:**
*   **Language:** Python (Object-Oriented Programming)
*   **Design Patterns Used (6 patterns used):**
    1.  **Singleton** (Creational): Used for the central `SmartCityController` to ensure a single point of access and control for the entire system.
    2.  **Facade** (Structural): Implemented in the `SmartCityController` to provide a simplified, high-level interface to the complex set of city subsystems.
    3.  **Factory Method** (Creational): Used in the `TransportManager` to create various types of traffic components (e.g., `TrafficLight`).
    4.  **Abstract Factory** (Creational): Used in the `LightingManager` to create families of related lighting components (e.g., `LEDLight` and `MotionSensor` from an `EnergyEfficientFactory`).
    5.  **Builder** (Creational): Used in the `EnergyManager` to construct complex, multi-part reports (e.g., `EnergyConsumptionReport`) step-by-step.
    6.  **Proxy** (Structural): Used in the `SecurityManager` to control access to sensitive operations (like initiating a full city patrol) based on user roles.

## Project Structure

The project is organized as a modular application following the recommended structure:

```
SmartCitySystem/
├── main.py                 # Main application entry point (Console Interface)
├── test.py                 # Unit tests for system components and patterns
├── core/                   # Core system components
│   ├── controller.py       # Central controller / Facade / Singleton
│   ├── factories/          # Factory Method and Abstract Factory implementations
│   │   ├── __init__.py
│   │   └── factory_method.py
│   ├── builders/           # Builder for step-by-step object construction
│   │   ├── __init__.py
│   │   └── report_builder.py
│   ├── adapters/           # (Not used in this implementation)
│   ├── proxy/              # Proxy for subsystem access control
│   │   ├── __init__.py
│   │   └── proxy.py
│   ├── singleton/          # Singleton for unique components
│   │   ├── __init__.py
│   │   └── singleton.py
│   └── __init__.py
├── modules/                # Smart city subsystems
│   ├── transport/          # Transportation management (Uses Factory Method)
│   │   ├── __init__.py
│   │   └── manager.py
│   ├── lighting/           # Lighting management (Uses Abstract Factory)
│   │   ├── __init__.py
│   │   └── manager.py
│   ├── security/           # Security subsystem (Uses Proxy)
│   │   ├── __init__.py
│   │   └── manager.py
│   ├── energy/             # Energy saving and monitoring (Uses Builder)
│   │   ├── __init__.py
│   │   └── manager.py
│   └── __init__.py
└── README.md               # Assignment description and project structure
```

## How to Run

1.  Navigate to the project directory:
    ```bash
    cd SmartCitySystem
    ```
2.  Run the main application:
    ```bash
    python3 main.py
    ```
3.  Follow the on-screen console menu to interact with the SmartCity System.

## How to Run Tests

1.  Navigate to the project directory:
    ```bash
    cd SmartCitySystem
    ```
2.  Run the unit tests:
    ```bash
    python3 test.py
    ```
    (Expected output: All tests should pass, confirming the correct implementation of the design patterns and subsystem logic.)
