import requests

url = "https://10.10.20.90:443/dataservice/statistics/interface"

payload = {}
headers = {
  'X-XSRF-TOKEN': '66F58D27097E99119041BDE2B1FB872ADEF11699876EE60219F2C0007863BA435C1EEB58F6A24FE7E08220E75BEF7C5A0550',
  'Cookie': 'JSESSIONID=yxfWMPvzdMdTkHNIGS2WIwd8yrYjPU0HfUWYZQL-.81ac6722-a226-4411-9d5d-45c0ca7d567b'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)