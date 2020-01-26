import requests
import json

base = input("Convert from currency : ")
to = input("to currency : ")
amount = float(input("Amount : "))

url = 'https://api.exchangeratesapi.io/latest?base=' + base
response = requests.get(url)
data = response.text
parsed = json.loads(data)
rates = parsed["rates"]

for currency, rate in rates.items():
	if currency == to:
		conversion = rate * amount  # คำนวณหาจำนวนเงิน
		print("1 {} = {} {:,.2f}".format(base, currency, rate))
		print("{} {} = {} {:,.2f}".format(amount, base, currency, conversion))