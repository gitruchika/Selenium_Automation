import json

def read_json_data(filename):
    with open(filename) as file:
        data = json.load(file)
        return data


user_data = read_json_data("test_json_data.json")
for val in user_data['emp_details']:
    print(val['name'])