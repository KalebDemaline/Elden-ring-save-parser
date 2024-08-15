from Dicts.long import test

import requests

url = 'https://eldenring.fanapis.com/api/weapons'

data = ['id', 'name', 'rarity', 'category', 'weight']

with open('Dicts/edited.py', 'w') as f:
    print("new_dict = {", file=f)
    for _, item in test.items():
        print(f"\t\"{item['full_hex_id']}\": {{", file=f)
        for elements in data:
            print(f"\t\t\"{elements}\": \"{item[elements]}\",", file=f)
        item_name = item['name']
        response = requests.get(f'{url}?name={item_name}')
        if response.json()['success'] == True:
            for res in response.json()['data']:
                if res['name'] == item_name:
                    image = res['image']
                    print(f"\t\t\"icon\": \"{image}\",", file=f)
        print("\t\t\"owned\": False", file=f)
        print("\t},", file=f)
    print("}", file=f)