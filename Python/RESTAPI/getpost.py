import requests

r = requests.get('http://httpbin.org/basic-auth/python/testing', auth=('python', 'testing'))

print(r.text)
print(r)

# for delaying the response 

ru = requests.get('http://httpbin.org/delay/1', timeout=3)


print(r.text)
