import requests
#pip install request from it came

response =requests.get("https://www.youtube.com")
print(response.text)