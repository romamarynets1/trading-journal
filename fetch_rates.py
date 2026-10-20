import sqlite3
import requests
url = "https://api.frankfurter.dev/v1/latest?base=USD&symbols=EUR,GBP,JPY"
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print("Помилка запиту:", e)
    raise SystemExit(1)
conn = sqlite3.connect("trades.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS rates (
    rate_date TEXT NOT NULL,
    base TEXT NOT NULL,
    currency TEXT NOT NULL,
    rate REAL NOT NULL,
    UNIQUE (rate_date, base, currency)
)
""")
for currency, rate in data["rates"].items():
    cur.execute(
        "INSERT OR IGNORE INTO rates (rate_date, base, currency, rate) VALUES (?, ?, ?, ?)",
        (data["date"], data["base"], currency, rate)
    )
conn.commit()
conn.close()
print("Збережено курсів за", data["date"])