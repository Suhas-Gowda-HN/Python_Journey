karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}

print(karnataka_food.keys())  # Output: dict_keys(['Bengaluru', 'Mysuru', 'Mangaluru'])

print(karnataka_food.values())  # Output: dict_values(['Bisi Bele Bath', 'Mysore Pak', 'Neer Dosa'])

print(karnataka_food.items())  # Output: dict_items([('Bengaluru', 'Bisi Bele Bath'), ('Mysuru', 'Mysore Pak'), ('Mangaluru', 'Neer Dosa')])

new_dishes = {"Hubballi": "Girmit"}
karnataka_food.update(new_dishes)
print(karnataka_food)
