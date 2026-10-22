import sqlite3
from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
app = FastAPI()
def get_conn():
    conn = sqlite3.connect("trades.db")
    conn.row_factory = sqlite3.Row
    return conn
@app.get("/")
def home():
    return {"message": "Привіт, це мій API"}
@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Привіт, {name}"}
@app.get("/trades")
def get_trades(pair: str | None = None):
    conn = get_conn()
    cur = conn.cursor()
    if pair:
        cur.execute(
            "SELECT id, pair, result, trade_date FROM trades WHERE pair = ? ORDER BY id",
            (pair.upper(),)
        )
    else:
        cur.execute("SELECT id, pair, result, trade_date FROM trades  ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]
@app.get("/rates")
def get_rates(currency: str | None = None):
    conn = get_conn()
    cur = conn.cursor()
    if currency:
        cur.execute(
            "SELECT rate_date, currency, rate FROM rates WHERE currency = ? ORDER BY rate_date",
            (currency.upper(),)
        )
    else:
        cur.execute("SELECT rate_date, currency, rate FROM rates ORDER BY rate_date")
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]
class TradeIn(BaseModel):
    pair: str
    result: float
    trade_date: str | None = None
@app.post("/trades")
def add_trades(trade: TradeIn):
    pair = trade.pair.upper()
    trade_date = trade.trade_date or date.today().isoformat()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO trades (pair, result, trade_date) VALUES (?, ?, ?)",
        (pair,trade.result, trade_date)
    )
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return {"id": new_id, "pair": pair, "result": trade.result, "trade_date": trade_date}
@app.get("/stats")
def get_stats():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*), SUM(result), MAX(result), MIN(result) FROM trades")
    count, total, best, worst = cur.fetchone()
    cur.execute("SELECT COUNT(*) FROM trades WHERE result > 0")
    wins = cur.fetchone()[0]
    conn.close()
    winrate = round(wins / count * 100, 1) if count else 0
    return {
        "trades": count,
        "total": total,
        "winrate": winrate,
        "best": best,
        "worst": worst,
    }
@app.get("/stats/by-pair")
def get_stats_by_pair():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT pair, COUNT(*) AS trades_count, SUM(result) AS total "
    "FROM trades GROUP BY pair ORDER BY total DESC"
    )
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]
app.mount("/app", StaticFiles(directory="static", html=True), name="static")