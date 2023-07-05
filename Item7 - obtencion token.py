import requests

url = "https://10.10.20.90:8443/dataservice/client/token"

payload = {}
headers = {
  'Cookie': 'JSESSIONID=yxfWMPvzdMdTkHNIGS2WIwd8yrYjPU0HfUWYZQL-.81ac6722-a226-4411-9d5d-45c0ca7d567b'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)