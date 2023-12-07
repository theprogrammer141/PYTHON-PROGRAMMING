principal=1000.0
interest_rate=0.05

for years in range(1,11):
    amount_on_deposit=principal*(1+interest_rate)**years
    print(f"AMOUNT AFTER {years} years:${amount_on_deposit:.2f}")
