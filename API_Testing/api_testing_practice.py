import requests


server = "https://reqres.in/"

# Get API Call
# uri = "api/users?page=2"
# api_url = f"{server}{uri}"
# response = requests.get(api_url)
# print("status code:", response.status_code)
# print(response.json())
# res_data = response.json()
#
# for data in res_data['data']:
#     print(data['email'])
#
# Post API call
uri2 = "api/users"
input_data = {
    "name": "Ruchika",
    "job": "Scrum Master"
}
post_url = f"{server}{uri2}"
response_data = requests.post(post_url, data=input_data)
res_json = response_data.json()
print(res_json, response_data.status_code)
assert response_data.status_code == 201
assert res_json['job'] == 'Scrum Master1'
assert res_json['name'] == 'Ruchika'




