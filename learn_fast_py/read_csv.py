from csv import reader

with open("potions.csv") as f:
    content = reader(f)
    contents = []
    for cont in content:
        contents += cont

print(contents)

