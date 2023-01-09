import requests
#status code
r = requests.put('https://httpbin.org/put', data ={'key':'value'})

print(r)

print(r.text)