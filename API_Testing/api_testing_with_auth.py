import requests
from requests.auth import HTTPBasicAuth

username = ''
password = ''
response = requests.get('https://api.githuc.com/user,', auth = HTTPBasicAuth(username, password))

print(response.text)
print(response.json())