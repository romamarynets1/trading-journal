import json
trades = [
    {"pair": "EURUSD", "result": -100},
    {"pair": "GER40", "result": -100},
    {"pair": "EURUSD", "result": 0 },
    {"pair": "US100", "result": -100 },
    {"pair": "GBPUSD", "result": -100 },
    {"pair": "AUDUSD", "result": 200 },
    {"pair": "XAUUSD", "result": -100 },
]
with open("trades.json", "w", encoding="utf-8") as f:
    json.dump(trades, f, ensure_ascii=False, indent=2)
print("Збережено")
with open("trades.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded)
