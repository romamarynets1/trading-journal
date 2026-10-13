import json
with open("trades.json", "r", encoding="utf-8") as f:
    trades = json.load(f)
total = 0
wins = 0
best = 0
worst = 0
by_pair = {}
for trade in trades:
    total += trade["result"]
    if trade["result"] > 0:
        wins += 1
    if trade["result"] > best:
        best = trade["result"]
    if trade["result"] < worst:
        worst = trade["result"]
    if trade["pair"] not in by_pair:
        by_pair[trade["pair"]] = 0
    by_pair[trade["pair"]] += trade["result"]
winrate = round(wins / len(trades) * 100, 1)
print("Угод:", len(trades))
print("Загальний результат:", total)
print("Winrate:", winrate, "%")
print("Найкраща угода:", best)
print("Найгірша угода:", worst)
print("По парах:", by_pair)
