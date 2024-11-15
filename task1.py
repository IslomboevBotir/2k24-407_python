class Car:
    def __init__(self, car_type, models):
        self.car_type = car_type
        self.models = models


class Model:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Purchase:
    def __init__(self):
        self.cars = {
            1: Car("Sedan", [
                Model("Sedan Model A", 20000),
                Model("Sedan Model B", 22000),
                Model("Sedan Model C", 25000)
            ]),
            2: Car("Hetchbek", [
                Model("Hetchbek Model A", 18000),
                Model("Hetchbek Model B", 19500),
                Model("Hetchbek Model C", 21000)
            ]),
            3: Car("Kupe", [
                Model("Kupe Model A", 27000),
                Model("Kupe Model B", 30000),
                Model("Kupe Model C", 35000)
            ]),
            4: Car("Minivan", [
                Model("Minivan Model A", 23000),
                Model("Minivan Model B", 25000),
                Model("Minivan Model C", 27000)
            ]),
            5: Car("SUV", [
                Model("SUV Model A", 30000),
                Model("SUV Model B", 32000),
                Model("SUV Model C", 35000)
            ])
        }
        self.colors = {
            1: ("Qora", 0.02),
            2: ("Oq", 0.0),
            3: ("Kulrang", 0.01)
        }

    def select_car(self):
        print("Iltimos, quyidagi variantlardan mashina turini tanlang:")
        for key, car in self.cars.items():
            print(f"{key}. {car.car_type}")

        while True:
            try:
                car_choice = int(input("Tanlagan raqamingizni kiriting: "))
                if car_choice in self.cars:
                    selected_car = self.cars[car_choice]
                    print(f"Siz tanladingiz: {selected_car.car_type}")
                    return selected_car
                else:
                    print("Noto‘g‘ri tanlov. Iltimos, qaytadan urinib ko‘ring.")
            except ValueError:
                print("Iltimos, to'g'ri raqam kiriting.")

    def select_model(self, car):
        print(f"\n{car.car_type} uchun mavjud modellari:")
        for index, model in enumerate(car.models, start=1):
            print(f"{index}. {model.name} - ${model.price}")

        while True:
            try:
                model_choice = int(input("Model raqamini kiriting: "))
                if 1 <= model_choice <= len(car.models):
                    selected_model = car.models[model_choice - 1]
                    print(f"Siz tanladingiz: {selected_model.name}")
                    return selected_model
                else:
                    print("Noto‘g‘ri tanlov. Iltimos, qaytadan urinib ko‘ring.")
            except ValueError:
                print("Iltimos, to'g'ri raqam kiriting.")

    def select_color(self):
        print("\nMavjud ranglar:")
        for key, (color, extra) in self.colors.items():
            print(f"{key}. {color} ({extra * 100:.0f}% qo‘shimcha narx)")

        while True:
            try:
                color_choice = int(input("Rang raqamini kiriting: "))
                if color_choice in self.colors:
                    selected_color, extra = self.colors[color_choice]
                    print(f"Siz tanladingiz: {selected_color}")
                    return selected_color, extra
                else:
                    print("Noto‘g‘ri tanlov. Iltimos, qaytadan urinib ko‘ring.")
            except ValueError:
                print("Iltimos, to'g'ri raqam kiriting.")

    def confirm_purchase(self, car, model, color, base_price, final_price):
        print("\nTanlovingizni tasdiqlang:")
        print(f"Tur: {car.car_type}")
        print(f"Model: {model.name}")
        print(f"Rang: {color}")
        print(f"Asosiy narx: ${base_price:.2f}")
        print(f"Yakuniy narx (rang qo'shimchasi bilan): ${final_price:.2f}")
        confirm = input("Sotib olishni davom ettirasizmi? (ha/yo'q): ").lower()
        if confirm == 'ha':
            print("\nSotib olish tasdiqlandi!")
            print(f"\nTo'lovni amalga oshirish...\n${final_price:.2f} summasidagi to'lov muvaffaqiyatli amalga oshirildi!")
            print("Sotib olganingiz uchun rahmat.")
        else:
            print("Sotib olish bekor qilindi.\nHech qanday sotib olish amalga oshirilmadi.")

    def run(self):
        selected_car = self.select_car()
        selected_model = self.select_model(selected_car)
        selected_color, extra = self.select_color()
        
        base_price = selected_model.price
        final_price = base_price * (1 + extra)
        
        self.confirm_purchase(selected_car, selected_model, selected_color, base_price, final_price)


if __name__ == "__main__":
    purchase = Purchase()
    purchase.run()
