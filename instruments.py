import sqlite3
conn = sqlite3.connect("trades.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS instruments (pair TEXT PRIMARY KEY, category TEXT NOT NULL)""")
data = [
    ("EURUSD", "Forex"),
    ("GBPUSD", "Forex"),
    ("AUDUSD", "Forex"),
    ("XAUUSD", "Metals"),
    ("GER40", "Indices"),
    ("US100", "Indices"),
]
for pair, category in data:
    cur.execute("INSERT OR IGNORE INTO instruments (pair, category) VALUES (?, ?)", (pair, category))
conn.commit()
conn.close()
print("Готово")
