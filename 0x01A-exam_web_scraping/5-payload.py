import requests

details = {"name": "John Doe", "age": 30, "email": "johndoe@example.com"}

url_post = "https://api.example.com/submit"
#a post request to the api
post_response = requests.post(url_post, json=details)
#printing out the response
post_response_json = post_response.json()
print(post_response_json)