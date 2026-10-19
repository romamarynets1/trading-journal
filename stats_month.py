import sqlite3
conn = sqlite3.connect("trades.db")
cur = conn.cursor()
cur.execute("""
SELECT strftime('%Y-%m', trade_date) AS month, COUNT(*) AS trades_count, SUM(result) as total FROM trades GROUP BY month ORDER BY month""")
for row in cur.fetchall():
    print(row)
conn.close()