class CarModel:
    def __init__(self, model_name, price):
        self.model_name = model_name
        self.price = price

    def __str__(self):
        return f"{self.model_name} - ${self.price}"


class CarType:
    def __init__(self, type_name, models):
        self.type_name = type_name
        self.models = models

    def display_models(self):
        print(f"Available models for {self.type_name}:")
        for idx, model in enumerate(self.models, 1):
            print(f"{idx}. {model}")

    def get_model(self, model_number):
        return self.models[model_number - 1]


class Car:
    def __init__(self, car_type, model, color):
        self.car_type = car_type
        self.model = model
        self.color = color
        self.price = model.price

    def display_summary(self):
        print(f"\nYou have selected the following car:")
        print(f"Type: {self.car_type.type_name}")
        print(f"Model: {self.model.model_name}")
        print(f"Color: {self.color}")
        print(f"Price: ${self.price}")


def main():
    # Available car types and models
    sedan_models = [CarModel("Sedan Model A", 25000), CarModel("Sedan Model B", 27000)]
    hatchback_models = [CarModel("Hatchback Model A", 20000), CarModel("Hatchback Model B", 22000)]
    coupe_models = [CarModel("Coupe Model A", 30000), CarModel("Coupe Model B", 32000)]
    minivan_models = [CarModel("Minivan Model A", 35000), CarModel("Minivan Model B", 37000)]
    suv_models = [CarModel("SUV Model A", 45000), CarModel("SUV Model B", 47000)]

    car_types = [
        CarType("Sedan", sedan_models),
        CarType("Hatchback", hatchback_models),
        CarType("Coupe", coupe_models),
        CarType("Minivan", minivan_models),
        CarType("SUV", suv_models),
    ]

   
    print("Select Car Type:")
    for idx, car_type in enumerate(car_types, 1):
        print(f"{idx}. {car_type.type_name}")

    car_type_choice = int(input("\nEnter the number of your choice: "))
    selected_car_type = car_types[car_type_choice - 1]


    selected_car_type.display_models()
    model_choice = int(input("\nEnter the number of your choice: "))
    selected_model = selected_car_type.get_model(model_choice)


    print("\nSelect Color:")
    colors = ["Black", "White", "Gray"]
    for idx, color in enumerate(colors, 1):
        print(f"{idx}. {color}")
    color_choice = int(input("\nEnter the number of your choice: "))
    selected_color = colors[color_choice - 1]


    car = Car(selected_car_type, selected_model, selected_color)
    car.display_summary()


    confirm = input("\nDo you want to confirm the purchase? (yes/no): ").strip().lower()
    if confirm == "yes":
        print(f"\nYour purchase has been completed! Final price: ${car.price}")
    else:
        print("\nPurchase canceled.")


if __name__ == "__main__":
    main()
