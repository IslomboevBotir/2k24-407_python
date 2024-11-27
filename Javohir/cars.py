cars = {
    "sedan": {
        "Toyota Camry": 25000,
        "Honda Accord": 24000,
        "Hyundai Sonata": 23000
    },
    "hatchback": {
        "Volkswagen Golf": 22000,
        "Ford Fiesta": 18000,
        "Kia Rio": 17000
    },
    "coupe": {
        "Chevrolet Camaro": 35000,
        "Ford Mustang": 37000,
        "Dodge Challenger": 38000
    },
    "minivan": {
        "Toyota Sienna": 30000,
        "Honda Odyssey": 31000,
        "Kia Carnival": 32000
    },
    "suv": {
        "Toyota RAV4": 27000,
        "Honda CR-V": 26000,
        "Ford Explorer": 35000
    }
}

available_colors = ["qora", "oq", "seriy"]


def choose_car_type():
    print("Moshingiz turini tanlang:")
    car_types = list(cars.keys())
    for idx, car_type in enumerate(car_types, start=1):
        print(f"{idx}. {car_type.capitalize()}")

    try:
        choice = int(input("\nKerakli tur raqamini tanlang: ")) - 1
        if 0 <= choice < len(car_types):
            return car_types[choice]
        else:
            raise ValueError
    except ValueError:
        print("Yaroqsiz tanlov. Iltimos, qayta urinib koʻring.")
        return choose_car_type()


def choose_car_model(car_type):
    print(f"\n{car_type.capitalize()} uchun mavjud modellar:")
    car_models = list(cars[car_type].items())
    for idx, (model, price) in enumerate(car_models, start=1):
        print(f"{idx}. {model} (${price})")

    try:
        choice = int(input("\nKerakli model raqamini tanlang: ")) - 1
        if 0 <= choice < len(car_models):
            model, price = car_models[choice]
            return model, price
        else:
            raise ValueError
    except ValueError:
        print("Yaroqsiz model. Iltimos, qayta urinib koʻring.")
        return choose_car_model(car_type)


def choose_color():
    print("\nRangini tanlang:")
    for idx, color in enumerate(available_colors, start=1):
        print(f"{idx}. {color.capitalize()}")

    try:
        choice = int(input("\nKerakli rang raqamini tanlang: ")) - 1
        if 0 <= choice < len(available_colors):
            return available_colors[choice]
        else:
            raise ValueError
    except ValueError:
        print("Yaroqsiz rang. Iltimos, qayta urinib koʻring.")
        return choose_color()


def confirm_selection(car_type, model, color):
    print("\nSizning tanlovingiz xulosasi:")
    print(f"Moshinga turi: {car_type.capitalize()}")
    print(f"Modeli: {model}")
    print(f"Rangi: {color.capitalize()}")
    confirm = input("\nBu xaridni davom ettirmoqchimisiz? (ha/yo'q): ").lower()
    return confirm == "ha"


def main():
    print("Avtomobil tanlash tizimiga xush kelibsiz!")

    car_type = choose_car_type()
    model, price = choose_car_model(car_type)
    color = choose_color()

    if confirm_selection(car_type, model, color):
        print(f"\nTabriklaymiz! Siz muvaffaqiyatli xarid qildingiz: {color.capitalize()} {model}.")
        print(f"Umumiy narx: ${price}. Haridingiz uchun rahmat!")
    else:
        print("\nXarid bekor qilindi. Tashrifingiz uchun rahmat!")


def confirm_selection(car_type, model, color):
    print("\nSizning tanlovingiz xulosasi:")
    print(f"Moshinga turi: {car_type.capitalize()}")
    print(f"Modeli: {model}")
    print(f"Rangi: {color.capitalize()}")

    while True:
        confirm = input("\nBu xaridni davom ettirmoqchimisiz? (ha/yoq): ").lower()
        if confirm in ["ha", "yoq"]:
            return confirm == "ha"
        else:
            print("Siz noto'g'ri javob berdingiz. Iltimos, 'ha' yoki 'yoq' deb javob bering.")


if __name__ == "__main__":
    main()
