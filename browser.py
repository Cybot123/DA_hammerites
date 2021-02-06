# Use the Request library
import requests
# Set the target webpage
url =input("enter your URL:")
r = requests.get(url)
# This will get the full page
print(r.text)
# This will get the status code
print("Status code:")
print("\t *", r.status_code)
