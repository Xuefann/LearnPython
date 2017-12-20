import urllib.request

req = urllib.request.Request('http://placekitten.com/g/450/450')
response = urllib.request.urlopen(req)

cat_img = response.read()

with open('cat_.jpg','wb') as f:
	f.write(cat_img)