import sqlite3
conn = sqlite3.connect("trades.db")
cur = conn.cursor()
cur.execute("CREATE INDEX IF NOT EXISTS idx_trades_pair ON trades(pair)")
cur.execute("CREATE INDEX IF NOT EXISTS idx_trades_date ON trades(trade_date)")
conn.commit()
conn.close()
print("Індекси створено")