
# import requests
# r = requests.get('https://jsonplaceholder.typicode.com/posts')
# print(r.status_code)
# print(r.json())


import requests
res = requests.get('https://jsonplaceholder.typicode.com/posts')
print(res.status_code)
print(res.json())