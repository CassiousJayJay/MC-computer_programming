import requests

url = "https://api.example.com/data" 
#get request from the api
response = requests.get(url)
#print the response 
response_json = response.json()
print(response_json)

