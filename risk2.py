def calc_risk(deposit, risk_percent):
    return deposit * risk_percent / 100
while True:
    deposit = float(input("Депозит ($), 0 для виходу: "))
    if deposit == 0:
        break
    risk_percent = float(input("Ризик (%): "))
    risk_amount = calc_risk(deposit, risk_percent)
    print("Ти ризикуєш:", risk_amount, "$")
