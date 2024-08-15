from Backend.Dicts.armament_data_long import armament_data_dict

data = ['id', 'name', 'rarity', 'category', 'weight']

with open('Dicts/edited.py', 'w') as f:
    print("new_dict = {", file=f)
    for _, item in armament_data_dict.items():
        print(f"\t\"{item['full_hex_id']}\": {{", file=f)
        for elements in data:
            print(f"\t\t\"{elements}\": \"{item[elements]}\",", file=f)
        print("\t\t\"owned\": False", file=f)
        print("\t},", file=f)
    print("}", file=f)