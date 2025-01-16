class Car:
    def __init__(self, car_type, model, color, price):
        self.car_type = car_type
        self.model = model
        self.color = color
        self.price = price

    def display_info(self):
        print(f"Mashina turi: {self.car_type}\nModeli: {self.model}\nRangi: {self.color}\nNarxi: ${self.price}")


car_inventory = {
    'Sedan': [('Toyota Camry', 24000), ('Honda Accord', 26000)],
    'Xetchbek': [('Ford Fiesta', 18000), ('Volkswagen Golf', 22000)],
    'Kupe': [('BMW 2 Series', 35000), ('Audi A5', 42000)],
    'Miniven': [('Honda Odyssey', 32000), ('Toyota Sienna', 33000)],
    'SUV': [('Toyota RAV4', 29000), ('Honda CR-V', 31000)]
}

available_colors = ['Qora', 'Oq', 'Kulrang']


def get_choice(options, prompt):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        choice = input(prompt)
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("Noto'g'ri tanlov. Iltimos, qayta urinib ko'ring.")


def main():
    car_type = get_choice(list(car_inventory.keys()), "Mashina turini tanlang (raqamni kiriting): ")
    model, price = get_choice(car_inventory[car_type], f"{car_type} uchun modelni tanlang (raqamni kiriting): ")
    color = get_choice(available_colors, "Mashina rangini tanlang (raqamni kiriting): ")

    selected_car = Car(car_type, model, color, price)
    selected_car.display_info()

    if input("Xaridni davom ettirasizmi? (ha/yo'q): ").lower() == 'ha':
        print(f"\nXarid tasdiqlandi!\nYakuniy narx: ${selected_car.price}\nXaridingiz uchun rahmat!")
    else:
        print("Xarid bekor qilindi.")


if __name__ == "__main__":
    main()
