class Moshina:
    def __init__(self, car_type, model, color):
        self.car_type = car_type
        self.model = model
        self.color = color
        self.narxlar = {
            "Sedan": 20000,
            "Jip": 30000,
            "Hatchback": 15000,
            "Krossover": 25000
        }
        self.base_price = self.narxlar.get(self.car_type, 0)
        self.final_price = self.calculate_final_price()

    def calculate_final_price(self):
        additional_fees = 2000
        return self.base_price + additional_fees

    def yakuniy_malumot(self):
        print("\nSiz tanlagan moshina:")
        print(f"Tur: {self.car_type}")
        print(f"Nomi: {self.model}")
        print(f"Rang: {self.color}")
        print(f"Narxi: ${self.final_price:,} USD")


class CarDealership:
    def __init__(self):
        self.car_type = None
        self.model = None
        self.color = None
        self.selected_car = None

    def valid_input(self, prompt, options):
        while True:
            try:
                choice = int(input(prompt))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                else:
                    print(f"Xato! Iltimos, 1 dan {len(options)} gacha bo'lgan raqamni kiriting.")
            except ValueError:
                print("Xato! Faqat son kiriting.")

    def select_car_type(self):
        print("\nMoshina turini tanlang:")
        options = ["Sedan", "Jip", "Hatchback", "Krossover"]
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        self.car_type = self.valid_input("Tanlovni kiriting (1-4): ", options)

    def select_car_model(self):
        print("\nMoshina modelini tanlang:")
        models = ["Chevrolet Malibu", "Toyota Camry", "Kia Sportage", "Hyundai Tucson"]
        for i, model in enumerate(models, 1):
            print(f"{i}. {model}")
        self.model = self.valid_input("Tanlovni kiriting (1-4): ", models)

    def select_color(self):
        print("\nMoshina rangini tanlang:")
        colors = ["Qora", "Oq", "Qizil", "Ko'k"]
        for i, color in enumerate(colors, 1):
            print(f"{i}. {color}")
        self.color = self.valid_input("Tanlovni kiriting (1-4): ", colors)

    def confirm_selection(self):
        print("\nTanlangan ma'lumotlar:")
        print(f"Tur: {self.car_type}")
        print(f"Nomi: {self.model}")
        print(f"Rang: {self.color}")

    def complete_purchase(self):
        self.selected_car = Moshina(self.car_type, self.model, self.color)
        self.selected_car.yakuniy_malumot()


def main():
    dealership = CarDealership()
    dealership.select_car_type()
    dealership.select_car_model()
    dealership.select_color()
    dealership.confirm_selection()
    dealership.complete_purchase()


if __name__ == "__main__":
    main()
