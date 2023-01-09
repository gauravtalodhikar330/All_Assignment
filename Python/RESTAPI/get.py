import requests
#for pages

r = requests.get('https://httpbin.org/get')

# print(dir(r))
# print(help(r))
# print(r.text)
print(r.status_code)

#for image url

ri = requests.get('https://imgs.xkcd.com/comics/python.png')
# print(ri.content)
with open('comic.png', 'wb') as f:
    # For downloading the image we use content
    f.write(ri.content)
    print(ri.text)

print(ri.status_code)
print(r.ok)
print(r.headers)

# url to see
payload = {'page': 3, 'count': 2}
ru = requests.get('https://httpbin.org/get', params=payload)
# print(ru.text)
print(ru.url)

 