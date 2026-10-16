import sqlite3
conn = sqlite3.connect("trades.db")
cur = conn.cursor()
cur.execute("""SELECT i.category, COUNT(*), SUM(t.result) FROM trades t JOIN instruments i ON t.pair = i.pair GROUP BY i.category""")
for row in cur.fetchall():
    print(row)
conn.close()
