import sqlite3
conn = sqlite3.connect("trades.db")
cur = conn.cursor()
cur.execute("""SELECT i.category, COUNT(*) AS trades_count, SUM(t.result) AS total, ROUND(100.0 * SUM(CASE WHEN t.result > 0 THEN 1 ELSE 0 END) / COUNT(*), 1) AS winrate 
FROM trades t JOIN instruments i ON t.pair = i.pair GROUP BY i.category ORDER BY total DESC""")
for row in cur.fetchall():
    print(row)
conn.close()
