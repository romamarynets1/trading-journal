deposit = float(input("Депозит ($): "))
risk_percent = float(input("Ризик на угоду (%): "))
risk_amount = deposit * risk_percent / 100
print("Ти ризикуєш:", risk_amout, "$")
if risk_percent > 2:
    print("Увага: ризик більше 2% на угоду")
else:
    print("Ризик в межах норми")