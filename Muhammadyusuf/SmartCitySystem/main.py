import sys
import os
# Add the project root to the path to allow for relative imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.controller import get_controller

def display_menu():
    print("\n--- SmartCity System Console ---")
    print("1. Get All Subsystem Status")
    print("2. Run Simulation Cycle")
    print("3. Operate Specific Subsystem")
    print("4. Exit")
    print("--------------------------------")

def operate_subsystem_menu(controller):
    subsystems = controller.get_subsystem_names()
    print("\nAvailable Subsystems:")
    for i, name in enumerate(subsystems, 1):
        print(f"{i}. {name.capitalize()}")
    
    try:
        choice = input("Select subsystem number to operate: ")
        subsystem_index = int(choice) - 1
        if 0 <= subsystem_index < len(subsystems):
            subsystem_name = subsystems[subsystem_index]
            action = input(f"Enter action for {subsystem_name.capitalize()} (e.g., 'optimize_flow', 'run_patrol', 'report_consumption'): ")
            result = controller.operate_subsystem(subsystem_name, action.strip())
            print(f"\nOperation Result:\n{result}")
        else:
            print("Invalid subsystem number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    # The controller is a Singleton, so this call ensures we get the single instance.
    controller = get_controller()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            status = controller.get_all_status()
            print("\n--- All Subsystem Status ---")
            for name, stat in status.items():
                print(f"[{name.capitalize()}]: {stat}")
            print("----------------------------")
        
        elif choice == '2':
            status = controller.run_simulation()
            print("\n--- Final Status After Simulation ---")
            for name, stat in status.items():
                print(f"[{name.capitalize()}]: {stat}")
            print("-------------------------------------")

        elif choice == '3':
            operate_subsystem_menu(controller)

        elif choice == '4':
            print("Exiting SmartCity System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
