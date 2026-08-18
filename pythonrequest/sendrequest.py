#Note: pip install requests
import requests

r=requests.get('https://xkcd.com/353/')
#output Response 200
print(r)

print(dir(r))
#shows all attribute and method that we can run from this response r

print(help(r))

#give content orf response in unicode, we get some html here
print(r.text)


#Sends an HTTP GET request to the URL. Downloads the resource located at that URL image in byte. Stores the response in the variable p.
p = requests.get('https://imgs.xkcd.com/comics/python.png')
print(p.content)
#write this image in an file comic.png
with open('comic.png', 'wb') as f:
    f.write(p.content)

#to see sucees response comming any response may come 200 , 300, 500 etc
print(r.status_code)
print(r.ok)

#to see the headers
print(r.headers)


payload = {'page': 2, 'count': 25}
t = requests.get('https://httpbin.org/get', params=payload)

print(t.text)
#Output
# "args": {
#     "count": "25",
#     "page": "2"
# },
# "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.21.0"
# }


#to see url requested 
print(r.url)
#output
#https://httpbin.org/get?page=2&count=25



#for post form data request

payload2 = {
    'username': 'corey',
    'password': 'testing'
}

r1 = requests.post('https://httpbin.org/post', data=payload2)

print(r1.text)

#Response
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "password": "testing",
#     "username": "corey"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "32",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.21.0"
#   },
#   "json": null,
#   "url": "https://httpbin.org/post"
# }

r_dict = r1.json()
print(r_dict['form'])
#response it will give dictionery of that form
#{'password': 'testing', 'username': 'corey'}

#passing credential with basic authentication auth=(tuple)
r3 = requests.get('https://httpbin.org/basic-auth/corey/testing',auth=('corey', 'testing')
)

print(r3.text)
#Response
# {
#   "authenticated": true,
#   "user": "corey"
# }
print(3) #when credential incorrect 403 forbidden but when correct then 200


#This example demonstrates how to set a timeout for an HTTP request using the Python requests library.
r5 = requests.get('https://httpbin.org/delay/6', timeout=3)
#The /delay/6 endpoint intentionally waits 6 seconds before sending a response.
#"Wait at most 3 seconds for the server's response. If no response arrives within that time, raise an exception."
print(r5)