def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

x=int(input("ENTER X:"))
y=int(input("ENTER Y:"))
result = gcd(x,y)
print(f"THE GCD of {x} AND {y} IS: {result}")
