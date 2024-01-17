terms = int(input("ENTER NUMBER OF TERMS:"))
a = 0
b = 1
c = 0
for i in range(0, terms):
    print(a)
    c = a+b
    a = b
    b = c
