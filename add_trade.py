import json
import os
if os.path.exists("trades.json"):
    with open("trades.json", "r", encoding="utf-8") as f:
        trades = json.load(f)
else:
    trades = []
pair = input("Пара: ")
result = float(input("Результат: "))
trades.append({"pair": pair, "result": result})
with open("trades.json", "w", encoding="utf-8") as f:
    json.dump(trades, f, ensure_ascii=False, indent=2)
    print("Угоду додано. Усього угод:", len(trades))
    