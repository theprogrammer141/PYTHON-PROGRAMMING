largest=0
smallest=0

for i in range(5):
    num=int(input(f"ENTER NUMBER {i+1}:"))
    
if num>largest:
    largest=num
if num<smallest:
    smallest=num
    
print("LARGEST NUMBER:",largest)
print("SMALLEST NUMBER:",smallest)