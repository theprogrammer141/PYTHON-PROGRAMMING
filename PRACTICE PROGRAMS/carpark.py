def calculate_charges(hours_parked):
    minimum_fee=2.00
    additional_charge_rate=0.50
    additional_hours=max(0, hours_parked - 3)
    total_charge=min(minimum_fee+additional_hours*additional_charge_rate,10.00)
    return total_charge


total_receipts = 0.0
    
for customer in range(1, 4):
    hours_parked = float(input(f"ENTER THE NUMBER OF HOURS FOR CUSTOMER {customer}: "))
    charge = calculate_charges(hours_parked)
    total_receipts += charge

print(f"CUSTOMER {customer}:")
print(f"HOURS PARKED: {hours_parked}")
print(f"CHARGE: £{charge:.2f}\n")

print(f"TOTAL RECEIPTS FROM THREE CUSTOMERS: £{total_receipts:.2f}")