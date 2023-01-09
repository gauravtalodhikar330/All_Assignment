from urllib import response

import requests



payload = {'username': 'python', 'password':'testing'}

r = requests.post('https://httpbin.org/post', data=payload)

r_dict = r.json()

print(r.text)

print(r_dict['form'])
