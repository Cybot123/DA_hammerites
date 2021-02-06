# Use the Request library
import requests
# Set the target webpage
url = "http://www.wikipedia.org"
r = requests.get(url)
# This will just get just the headers
h = requests.head(url)
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
# This will modify the headers user-agent
headers = {
    'User-Agent' : "Redmi Note 8 Pro"
}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)

