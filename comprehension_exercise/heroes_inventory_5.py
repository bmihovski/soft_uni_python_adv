hero_names = input().split(", ")
heroes = {hero: {} for hero in hero_names}
while True:
    user_input = input()
    if user_input == "End":
        break
    name, item, price = user_input.split("-")
    if name in heroes:
        if item not in heroes[name]:
            heroes[name][item] = int(price)

{print(f"{hero} -> Items: {len(heroes[hero])}, Cost: {sum(weapon.values())}") for hero, weapon in heroes.items()}
