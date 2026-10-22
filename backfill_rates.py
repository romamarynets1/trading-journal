import sqlite3
import requests
url = "https://api.frankfurter.dev/v1/2026-01-01..?base=USD&symbols=EUR,GBP,JPY"
try:
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print("Помилка запиту:", e)
    raise SystemExit(1)
conn = sqlite3.connect("trades.db")
cur = conn.cursor()
added = 0
for rate_date, day_rates in data["rates"].items():
    for currency, rate in day_rates.items():
        cur.execute(
            "INSERT OR IGNORE INTO rates (rate_date, base, currency, rate) VALUES (?, ?, ?, ?)",
            (rate_date, data["base"], currency, rate)
        )
        added += cur.rowcount
conn.commit()
conn.close()
print("Додано нових курсів;", added)