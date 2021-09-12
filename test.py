import http.client

conn = http.client.HTTPSConnection("currency-converter5.p.rapidapi.com")

headers = {'x-rapidapi-host': "currency-converter5.p.rapidapi.com"}

conn.request("GET", "/currency/convert?format=json&from=USD&to=ILS&amount=1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))