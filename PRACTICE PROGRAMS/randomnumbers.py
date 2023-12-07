import random

def random_numbers():
    num1=random.randint(1,2)
    num2=random.randint(1,100)
    num3=random.randint(0,9)
    num4=random.randint(1000,1112)
    num5=random.randint(-1,1)
    num6=random.randint(-3,11)
    return num1,num2,num3,num4,num5,num6

num1,num2,num3,num4,num5,num6=random_numbers();

print("RANDOM NUMBERS:\n")
print(f"NUM1:{num1}")
print(f"NUM2:{num2}")
print(f"NUM3:{num3}")
print(f"NUM4:{num4}")
print(f"NUM5:{num5}")
print(f"NUM6:{num6}")
