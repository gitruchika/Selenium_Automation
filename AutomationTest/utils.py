import json

def get_json_data(filename='test_data.json'):
    with open(filename) as file:
        data = json.load(file)
        return data