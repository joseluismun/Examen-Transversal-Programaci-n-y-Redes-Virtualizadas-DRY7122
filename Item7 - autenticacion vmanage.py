import requests

url = "https://10.10.20.90:8443/j_security_check"

payload = 'j_username=admin&j_password=C1sco12345'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'JSESSIONID=hGlz_kXym1qDfjXYgZ6QDclT6jFR3QhDxAdE8fGN.81ac6722-a226-4411-9d5d-45c0ca7d567b'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)