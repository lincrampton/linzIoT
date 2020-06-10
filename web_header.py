#
# using http.client package to read contents of www.uci.edu landing page
# 
import http.client
url = "www.uci.edu"

connection = http.client.HTTPSConnection(url)

connection.request("GET", "/")
response = connection.getresponse()

print (response.read().decode('utf-8')[:1500]) 
