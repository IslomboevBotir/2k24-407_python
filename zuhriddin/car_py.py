class Car:
    def __init__(self, car_type, car_model, car_color, car_price):
        self.type = car_type
        self.model = car_model
        self.color = car_color
        self.price = car_price

    def confirmation(self):
        print(f"Type: {self.type}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
        confirmation1 = input("Do you wish to continue? (Y/N): ")
        match confirmation1:
            case "y":
                print("Please wait...!")
                print("Your order has been successfully confirmed...")
                print("Thank you for your purchase!")
            case "n":
                print("Your order has been canceled!")
            case _:
                print("Wrong input, please try again!")


def model_selection(car_type, car_models, car_prices):
    model_select = input("Which model would you like to use?")
    match model_select:
        case "1":
            car_model = car_models[0]
            car_price = car_prices[0]
        case "2":
            car_model = car_models[1]
            car_price = car_prices[1]
        case "3":
            car_model = car_models[2]
            car_price = car_prices[2]
        case _:
            print("Wrong Input")
            return model_selection(car_type, car_models, car_prices)
    return car_type, car_model, car_price


def color_selection(car_type, car_model, car_price):
    print("Available Colors: \n1)White (+3% extra)\n2)Black (+5% extra)\n3)Grey")
    color = int(input("Enter your choice: "))
    match color:
        case "1":
            car_color = "White"
            car_price += car_price * 0.03
        case "2":
            car_color = "Black"
            car_price += car_price * 0.05
        case "3":
            car_color = "Grey"
        case _:
            print("Invalid Color")
            return color_selection(car_type, car_model, car_price)
    return car_type, car_model, car_color, car_price


def main():
    print("Car Types: \n1)Sedan\n2)Hatchback\n3)Coupe\n4)Minivan\n5)SUV")
    type_select = input("Select your car type:")
    match type_select:
        case "1":
            car_type = "Sedan"
            car_models = ["BMW M5", "Tesla Model S", "Audi A6"]
            prices = [145000, 95000, 60000]
            print("Choose Model of Car: \n1)BMW M5\n2)Tesla Model S\n3)Audi A6")
            car_type, car_model, car_price = model_selection(car_type, car_models, prices)
            car_type, car_model, car_color, car_price = color_selection(car_type, car_model, car_price)
            car1 = Car(car_type, car_model, car_color, car_price)
            car1.confirmation()
        case "2":
            car_type = "Hatchback"
            car_models = ["Volkswagen Golf R", "Toyota Prius Prime", "Mini Hardtop"]
            prices = [45000, 90000, 75000]
            print("Choose Model of Car: \n1)Volkswagen Golf R\n2)Toyota Prius Prime\n3)MINI Hardtop")
            car_type, car_model, car_price = model_selection(car_type, car_models, prices)
            car_type, car_model, car_color, car_price = color_selection(car_type, car_model, car_price)
            car2 = Car(car_type, car_model, car_color, car_price)
            car2.confirmation()
        case "3":
            car_type = "Coupe"
            car_models = ["Aston Martin Vantage", "BMW M2", "McLaren Artura"]
            prices = [745000, 195000, 600000]
            print("Choose Model of Car: \n1)Aston Martin Vantage\n2)BMW M2\n3)McLaren Artura")
            car_type, car_model, car_price = model_selection(car_type, car_models, prices)
            car_type, car_model, car_color, car_price = color_selection(car_type, car_model, car_price)
            car3 = Car(car_type, car_model, car_color, car_price)
            car3.confirmation()
        case "4":
            car_type = "Minivan"
            car_models = ["Mercedes-Benz Sprinter Crew Van","Ford Transit Passenger Wagon","Chevrolet Express Passenger"]
            prices = [155000, 85000, 50000]
            print("Choose Model of Car: \n"
                  "1)Mercedes-Benz Sprinter Crew Van\n"
                  "2)Ford Transit Passenger Wagon\n"
                  "3)Chevrolet Express Passenger")
            car_type, car_model, car_price = model_selection(car_type, car_models, prices)
            car_type, car_model, car_color, car_price = color_selection(car_type, car_model, car_price)
            car4 = Car(car_type, car_model, car_color, car_price)
            car4.confirmation()
        case "5":
            car_type = "SUV"
            car_models = ["Lamborghini Urus", "BMW X6M", "Aston Martin DBX"]
            prices = [445000, 195000, 500000]
            print("Choose Model of Car: \n1)Lamborghini Urus\n2)BMW X6M\n3)Aston Martin DBX")
            car_type, car_model, car_price = model_selection(car_type, car_models, prices)
            car_type, car_model, car_color, car_price = color_selection(car_type, car_model, car_price)
            car5 = Car(car_type, car_model, car_color, car_price)
            car5.confirmation()
        case _:
            print("Invalid Input")


if __name__ == "__main__":
    main()
