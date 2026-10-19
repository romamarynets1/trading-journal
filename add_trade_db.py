import sqlite3
conn = sqlite3.connect("trades.db")
cur = conn.cursor()
pair = input("Пара: ").upper()
cur.execute("SELECT 1 FROM instruments WHERE pair = ?", (pair,))
if cur.fetchone() is None:
    category = input("Нова пара. Категорія (Forex/Metals/Indices): ").capitalize()
    cur.execute("INSERT INTO instruments (pair,category) VALUES (?, ?)", (pair,category))
while True:
    try:
        result = float(input("Результат: "))
        break
    except ValueError:
        print("Введи число, наприклад 75 або -30")
cur.execute("INSERT INTO trades (pair, result) VALUES (?, ?)", (pair, result))
conn.commit()
cur.execute("SELECT COUNT(*) FROM trades")
print("Угоду додано. Усього угод:", cur.fetchone()[0])
conn.close()