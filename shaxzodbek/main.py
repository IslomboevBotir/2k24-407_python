class CarDealership:
    def __init__(self):
        self.car_types = ['Sedan', 'Hatchback', 'Coupe', 'Minivan', 'SUV']
        self.models = {
            'Sedan': [
                {'model': 'Sedan Model A', 'price': 20000},
                {'model': 'Sedan Model B', 'price': 22000},
                {'model': 'Sedan Model C', 'price': 25000}
            ],
            'Hatchback': [
                {'model': 'Hatchback Model A', 'price': 18000},
                {'model': 'Hatchback Model B', 'price': 19500},
                {'model': 'Hatchback Model C', 'price': 21000}
            ],
            'Coupe': [
                {'model': 'Coupe Model A', 'price': 23000},
                {'model': 'Coupe Model B', 'price': 26000}
            ],
            'Minivan': [
                {'model': 'Minivan Model A', 'price': 28000},
                {'model': 'Minivan Model B', 'price': 32000}
            ],
            'SUV': [
                {'model': 'SUV Model A', 'price': 30000},
                {'model': 'SUV Model B', 'price': 35000},
                {'model': 'SUV Model C', 'price': 40000}
            ]
        }
        self.colors = ['Black', 'White', 'Gray']
        self.selected_car = None

    def select_car_type(self):
        print("Please select a car type from the following options:")
        for index, car_type in enumerate(self.car_types, start=1):
            print(f"{index}. {car_type}")
        while True:
            try:
                choice = int(input("Enter the number corresponding to your choice: "))
                if 1 <= choice <= len(self.car_types):
                    self.car_type = self.car_types[choice - 1]
                    print(f"You have selected: {self.car_type}")
                    break
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def select_car_model(self):
        print(f"\nAvailable models for {self.car_type}:")
        available_models = self.models[self.car_type]
        for index, model_info in enumerate(available_models, start=1):
            print(f"{index}. {model_info['model']} - ${model_info['price']}")
        while True:
            try:
                choice = int(input("Select a model by entering its number: "))
                if 1 <= choice <= len(available_models):
                    self.model_info = available_models[choice - 1]
                    print(f"You have selected: {self.model_info['model']}")
                    break
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def select_color(self):
        print("\nAvailable colors:")
        for index, color in enumerate(self.colors, start=1):
            if color == 'Black':
                print(f"{index}. {color} with 2 % extra money")
            if color == 'White':
                print(f"{index}. {color} with 0 % extra money")
            if color == 'Gray':
                print(f"{index}. {color} with 1 % extra money")
        while True:
            try:
                choice = int(input("Select a color by entering its number: "))
                if 1 <= choice <= len(self.colors):
                    self.color = self.colors[choice - 1]
                    print(f"You have selected: {self.color}")
                    break
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def calculate_final_price(self):
        base_price = self.model_info['price']
        if self.color == 'White':
            color_price_adjustment = 0
        elif self.color == 'Gray':
            color_price_adjustment = base_price * 0.01  # 1% increase
        elif self.color == 'Black':
            color_price_adjustment = base_price * 0.02  # 2% increase
        else:
            color_price_adjustment = 0  # Default case (should not occur)
        final_price = base_price + color_price_adjustment
        return final_price

    def confirm_selection(self):
        final_price = self.calculate_final_price()
        print("\nPlease confirm your selection:")
        print(f"Type: {self.car_type}")
        print(f"Model: {self.model_info['model']}")
        print(f"Color: {self.color}")
        print(f"Base Price: ${self.model_info['price']:.2f}")
        print(f"Final Price (after color adjustment): ${final_price:.2f}")
        while True:
            choice = input("Do you want to proceed with the purchase? (yes/no): ").lower()
            if choice == 'yes':
                self.selected_car = Car(
                    car_type=self.car_type,
                    model=self.model_info['model'],
                    color=self.color,
                    base_price=self.model_info['price'],
                    final_price=final_price
                )
                print("Purchase confirmed!")
                break
            elif choice == 'no':
                print("Purchase cancelled.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def complete_purchase(self):
        if self.selected_car:
            print("\nProcessing payment...")
            print(f"Payment of ${self.selected_car.final_price:.2f} completed successfully!")
            print("Thank you for your purchase.")
        else:
            print("No purchase to complete.")

def main():
    dealership = CarDealership()
    dealership.select_car_type()
    dealership.select_car_model()
    dealership.select_color()
    dealership.confirm_selection()
    dealership.complete_purchase()

if __name__ == "__main__":
    main()