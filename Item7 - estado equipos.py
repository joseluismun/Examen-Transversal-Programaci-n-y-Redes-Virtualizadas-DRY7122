import requests

url = "https://10.10.20.90:443/dataservice/device/monitor"

payload = {}
headers = {
  'Cookie': 'JSESSIONID=hGlz_kXym1qDfjXYgZ6QDclT6jFR3QhDxAdE8fGN.81ac6722-a226-4411-9d5d-45c0ca7d567b'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)