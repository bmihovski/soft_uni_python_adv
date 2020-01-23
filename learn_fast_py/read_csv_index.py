from csv import reader

with open("potions.csv") as f:
    csv_file_content = reader(f)
    csv_contents = []
    for cont in csv_file_content:
        csv_contents += cont

effect_inx = csv_contents.index("Draught of Peacef")

print(csv_contents[effect_inx])
