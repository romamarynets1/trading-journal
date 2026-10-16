import sqlite3
conn = sqlite3.connect("trades.db")
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM trades")
count = cur.fetchone()[0]
print("Угод:", count)
cur.execute("SELECT SUM(result) FROM trades")
print("Загальний результат:", cur.fetchone()[0])
cur.execute("SELECT COUNT(*) FROM trades WHERE result > 0")
wins = cur.fetchone()[0]
print("Winrate:", round(wins / count * 100, 1), "%")
cur.execute("SELECT MAX(result), MIN(result) FROM trades")
best, worst = cur.fetchone()
print("Найкраща угода:", best)
print("Найгірша угода:", worst)
cur.execute("SELECT pair, SUM(result) FROM trades GROUP BY pair")
for row in cur.fetchall():
    print(row)
conn.close()
