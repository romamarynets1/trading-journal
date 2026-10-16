import json
import sqlite3
conn = sqlite3.connect("trades.db")
cur = conn.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS trades ( id INTEGER PRIMARY KEY AUTOINCREMENT, pair TEXT NOT NULL, result REAL NOT NULL ) """)
with open("trades.json", "r", encoding="utf-8") as f:
    trades = json.load(f)
for t in trades:
    cur.execute("INSERT INTO trades (pair, result) VALUES (?, ?)", (t["pair"], t["result"]))
conn.commit()
print("Імпортовано угод:", len(trades))
conn.close()
