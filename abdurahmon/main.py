class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def select_type(my_car):
        car_types = {
            "1": ("Sedan", [("BMW M5", 25000), ("Audi RS", 9000), ("Malibu", 12000)]),
            "2": ("Hatchback", [("Opel Rocks", 7000), ("Toyota Corolla", 9000), ("Ford Focus", 12000)]),
            "3": ("Miniwen", [("Car Max", 23000), ("Sienna Hybrid", 25000), ("Odyssey", 29000)]),
            "4": ("Suv", [("Hyundai Tucson", 20000), ("Mazda CX", 15000), ("Kia Sportage", 15000)])
        }
        while True:
            print("Iltimos, mashina turini tanlang:")
            for key, (type_name, _) in car_types.items():
                print(f"{key} = {type_name}")
            turi = input()
            if turi in car_types:
                my_car["Type"], models = car_types[turi]
                print("\nModel variantlari:")
                for idx, (model_name, price) in enumerate(models, 1):
                    print(f"{idx}. {model_name} = ${price}")
                my_car["Models"] = models
                break
            else:
                print("Noto'g'ri tanlov. Qayta urinib ko'ring.")

    def select_model(self, my_car):
        models = my_car["Models"]
        while True:
            model = input("O'zingizga kerakli bo'lgan mashina modelini tanlang (1, 2, 3): ")
            if model in ["1", "2", "3"]:
                index = int(model) - 1
                selected_model = models[index]
                my_car["Model"] = selected_model[0]
                my_car["Price"] = selected_model[1]
                print(f"Sizning mashinangiz: {selected_model[0]}, narxi: ${selected_model[1]}")
                break
            else:
                print("Noto'g'ri tanlov. Qayta urinib ko'ring.")

    def select_color(self, my_car):
        colors = {
            "1": ("Black", 1.0),
            "2": ("White", 1.2),
            "3": ("Gray", 1.1)
        }
        print("\nRang variantlari:")
        for key, (color_name, multiplier) in colors.items():
            extra_cost = int((multiplier - 1) * my_car["Price"])
            print(f"{key}. {color_name} (+${extra_cost})")
        while True:
            color = input("Iltimos, kerakli rangni tanlang: ")
            if color in colors:
                my_car["Color"], multiplier = colors[color]
                my_car["Price"] *= multiplier
                print(f"Sizning mashinangiz: {my_car['Model']}, rangi: {my_car['Color']}, narxi: ${int(my_car['Price'])}")
                break
            else:
                print("Noto'g'ri tanlov. Qayta urinib ko'ring.")

def main():
    my_car = {"Type": "", "Model": "", "Color": "", "Price": 0}
    print("Asalomu aleykum hurmatli mijoz!")
    car = Car("", 0)
    car.select_type(my_car)
    car.select_model(my_car)
    car.select_color(my_car)

    buy = input("Mashina sotib olishni xohlaysizmi? (yes/no): ").lower()
    if buy == "yes":
        print(f"Iltimos, to'lov qiling. Sizdan ${int(my_car['Price'])} talab qilinadi.")
        while True:
            tolov = input("To'lov qilish uchun 1 ni bosing yoki 'exit' deb yozing: ")
            if tolov == "1":
                print("Xaridingiz uchun rahmat!")
                break
            elif tolov == "exit":
                print("Tashrifingiz uchun rahmat!")
                break
            else:
                print("Noto'g'ri kiritingiz, qayta urinib ko'ring.")
    else:
        print("Tashrifingiz uchun rahmat! Yana kutib qolamiz.")

if __name__ == "__main__":
    main()
