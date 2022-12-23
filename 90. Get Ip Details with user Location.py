import requests
api_find_url = 'https://api.ipify.org?format=json'
res = requests.get(api_find_url)
if res.status_code == 200:
    data = res.json()
    # print(data)
    ip = data.get('ip')
    # print(ip)

ip_location_url = f'https://ipapi.co/{ip}/json/'
# print(ip_location_url)
r = requests.get(ip_location_url)
if r.status_code == 200:
    # print(r.json())
    ip_details = r.json()
    city = ip_details.get('city')
    region = ip_details.get('region')
    country_name = ip_details.get('country_name')

sentence = f'ip ({ip}) is located in {city} {region} , {country_name}'
print(sentence)
