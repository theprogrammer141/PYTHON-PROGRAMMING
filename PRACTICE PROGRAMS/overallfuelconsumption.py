total_liters=0.0
total_kilometers=0.0
tank_count=0

while True:
    liters=float(input("ENTER THE LITERS USED(-1 TO END):"))
    if liters==-1:
        break
       
    kilometers=float(input("ENTER THE KILOMETERS DRIVEN:"))

    fuel_consumption=(liters/kilometers)*100
    print(f"THE LITERS PER 100KM FOR THIS DRIVE WERE:{fuel_consumption:.1f}\n")

    total_liters=total_liters+liters
    total_kilometers=total_kilometers+kilometers
    tank_count=tank_count+1



if tank_count>0:
    overall_fuel_consumption=(total_liters/total_kilometers)*100
    print(f"THE OVERALL AVERAGE FUEL CONSUMPTION WAS:{overall_fuel_consumption:.1f}")
else:
    print("NO RECORD FOUND")

