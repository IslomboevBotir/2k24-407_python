cars = {
    "sedan": {
        "Toyota Camry": 30000,
        "Honda Accord": 28000,
        "Hyundai Sonata": 27000,
    },
    "hatchback": {
        "Volkswagen Golf": 25000,
        "Ford Focus": 22000,
        "Mazda 3": 23000,
    },
    "coupe": {
        "BMW 4 Series": 45000,
        "Audi A5": 43000,
        "Chevrolet Camaro": 37000,
    },
    "minivan": {
        "Chrysler Pacifica": 35000,
        "Honda Odyssey": 34000,
        "Toyota Sienna": 36000,
    },
    "SUV": {
        "Toyota RAV4": 32000,
        "Honda CR-V": 31000,
        "Ford Explorer": 40000,
    },
}


def input_number(txt, max_num):
    while True:
        selected_model = input(txt)
        if selected_model.isdigit():
            selected_num = int(selected_model)
            if 1 <= selected_num <= max_num:
                return selected_num
            elif selected_num > max_num:
                print(f"Error: Enter a number up to {max_num}!")
            else:
                print("Error: Enter a number greater than 0!")
        else:
            print("Enter numbers only!")


def select_car_model(cars):
    models_list = []
    print("\n========================================")
    print("            Select a Model              ")
    print("========================================")
    for index, model in enumerate(cars, start=1):
        models_list.append(model)
        print(f"{index} - {model}")
    print("========================================")
    num = input_number("\nEnter model ID number: ", len(models_list))
    return models_list[num - 1]


def car_name(cars):
    car_model = select_car_model(cars)
    car_list = list(cars[car_model].items())

    print(f"\nSelected model: {car_model}")
    print("\n========================================")
    print("            Select a Car                ")
    print("========================================")
    for index, (car, price) in enumerate(car_list, start=1):
        print(f"{index} - {car}: ${price}")
    print("========================================")
    num = input_number("\nEnter car ID number: ", len(car_list))

    selected_car, price = car_list[num - 1]
    return [car_model, selected_car, price]


def select_color(order_info):
    color_list = ["Black", "White", "Gray"]
    print("\n========================================")
    print("           Choose a Color               ")
    print("========================================")
    print(f"Model: {order_info[0]}\nCar: {order_info[1]}\nPrice: ${order_info[2]}")
    for i, color in enumerate(color_list, start=1):
        print(f"{i} - {color}")
    print("========================================")
    num = input_number("\nEnter color ID number: ", len(color_list))
    return color_list[num - 1]


def payment(car_info, color):
    print("\n========================================")
    print("            Review Details              ")
    print("========================================")
    print(
        f"Model: {car_info[0]}\nCar: {car_info[1]}\nPrice: ${car_info[2]}\nColor: {color}"
    )
    print("========================================")
    print("Do you want to buy the car?\n\n1 - Yes\n2 - No")
    confirm_payment = input_number("\nChoose 1 or 2: ", 2)

    if confirm_payment == 1:
        print("\n========================================")
        print("          Select Payment Method         ")
        print("========================================")
        print("1 - Cash\n2 - Card")
        num = input_number("\nChoose 1 or 2: ", 2)
        payment_method = "Cash" if num == 1 else "Card"
        sales_information(payment_method, car_info, color)
    else:
        print("\n========================================")
        print("          Operation Canceled!           ")
        print("========================================")


def sales_information(payment_method, car_info, color):
    print("\n========================================")
    print("          Payment Confirmation          ")
    print("========================================")
    print(
        f"Payment method: {payment_method}\nModel: {car_info[0]}\nCar: {car_info[1]}\nColor: {color}\nPrice: ${car_info[2]}\nTotal amount paid: ${car_info[2]}"
    )
    print("========================================\n")


print("========================================")
print("     Welcome to the Car Selection Program     ")
print("========================================\n")
info = car_name(cars)
color = select_color(info)
payment(info, color)
