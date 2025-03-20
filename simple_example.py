import requests

url = "https://reqres.in/api/{resource}?page=1&per_page=1"

response_1 = requests.request("GET", url)
response_2 = requests.get(url)

assert 'cerulean' in response_1.text
print(response_1.text)

assert 'cerulean' in response_2.text
print(response_2.text)