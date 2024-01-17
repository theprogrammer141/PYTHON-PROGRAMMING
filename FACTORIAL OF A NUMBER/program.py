# fact=1
# num=int(input("ENTER A NUMBER:"))
# i=1
# while(i<=num):
#     fact=fact*i
#     i=i+1
#
# print(f"THE FACTORIAL OF {num} IS {fact}")

def factorial(num):
    fact=1
    i=1
    while i <= num:
        fact=fact*i
        i=i+1
    print(f"THE FACTORIAL OF {num} IS {fact}")

number=int(input("ENTER A NUMBER:"))
factorial(number)