import sqlite3
conn = sqlite3.connect("trades.db")
cur = conn.cursor()
cur.execute("ALTER TABLE trades ADD COLUMN trade_date TEXT")
cur.execute("UPDATE trades SET trade_date = date('now') WHERE trade_date IS NULL")
conn.commit()
conn.close()
print("Готово")