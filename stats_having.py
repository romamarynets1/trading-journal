import sqlite3
conn = sqlite3.connect("trades.db")
cur = conn.cursor()
cur.execute("""
SELECT pair, COUNT(*) AS trades_count, SUM(result) AS total FROM trades GROUP BY pair HAVING COUNT(*) > 1 ORDER BY total DESC""")
for row in cur.fetchall():
    print(row)
conn.close()