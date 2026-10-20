import sqlite3
conn = sqlite3.connect("trades.db")
cur = conn.cursor()
cur.execute("SELECT * FROM rates")
for row in cur.fetchall():
    print(row)
conn.close()