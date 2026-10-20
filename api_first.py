import requests
url = "https://api.frankfurter.dev/v1/latest?base=USD&symbols=EUR,GBP,JPY"
response = requests.get(url, timeout=10)
print("Статус:", response.status_code)
data = response.json()
print(data)
print("Дата:", data["date"])
for currency, rate in data["rates"].items():
    print(currency, rate)