import random

car_types = ['Sedan', 'Hatchback', 'Coupe', 'Minivan', 'SUV']
models = {
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
colors = ['Black', 'White', 'Gray']

data_list = []

for _ in range(100):
    car_type = random.choice(car_types)
    model_info = random.choice(models[car_type])
    color = random.choice(colors)
    data_entry = {
        'type': car_type,
        'model': model_info['model'],
        'color': color,
        'price': model_info['price']
    }
    data_list.append(data_entry)
