import sqlite3
conn = sqlite3.connect("trades.db")
cur = conn.cursor()
cur.execute("""
SELECT currency,
       COUNT(*) AS days,
       ROUND(AVG(rate), 4) AS avg_rate,
       MIN(rate) AS min_rate,
       MAX(rate) AS max_rate
FROM rates
GROUP BY currency
""")
for row in cur.fetchall():
    print(row)
conn.close()