import json
from collections import defaultdict

def group_users_by_city(input_file, output_file):
    # 1. Read the source JSON file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            users = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: File '{input_file}' contains invalid JSON.")
        return

    # 2. Group users by city
    cities_dict = defaultdict(list)

    for user in users:
        city = user.get('address', {}).get('city')
        name = user.get('name')

        if city and name:
            cities_dict[city].append(name)

    result = dict(cities_dict)

    # 3. Save the result to a new JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print(f"Done! Data has been grouped and saved to '{output_file}'.")
    print(f"Cities found: {len(result)}")

if __name__ == "__main__":
    INPUT_FILE = 'users.json'
    OUTPUT_FILE = 'cities.json'

    group_users_by_city(INPUT_FILE, OUTPUT_FILE)