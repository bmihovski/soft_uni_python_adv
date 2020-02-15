categories = input().split(", ")
storage_cont = {cat: {} for cat in categories}
num_items = int(input())


def display_storage(num, food_categories):
    for _ in range(num):
        input_str = input()
        srt_mod = input_str.split(" - ")
        main_item = srt_mod[0]
        sub_item = srt_mod[1]
        item_props = srt_mod[2].split(";")
        item_quant = item_props[0].split(":")
        item_quant_name = item_quant[0]
        item_quant_value = int(item_quant[1])
        item_qual = item_props[1].split(":")
        item_qual_name = item_qual[0]
        item_qual_value = int(item_qual[1])
        if sub_item in food_categories:
            food_categories[main_item].update({sub_item: {item_quant_name: item_quant_value,
                                                          item_qual_name: item_qual_value}},)
        food_categories[main_item][sub_item] = {item_quant_name: item_quant_value, item_qual_name: item_qual_value}

    print(f"Count of items: "
          f"{sum([sum([food_spec['quantity'] for food_spec in food_type.values()]) for food_type in food_categories.values() if food_type])}")
    print(f"Average quality: "
          f"{sum([sum([food_spec['quality'] for food_spec in food_type.values()]) for food_type in food_categories.values() if food_type]) / len(categories):.2f}")
    {print(f"{cat} -> {', '.join(sub_cat.keys())}")for cat, sub_cat in food_categories.items()}


display_storage(num_items, storage_cont)
