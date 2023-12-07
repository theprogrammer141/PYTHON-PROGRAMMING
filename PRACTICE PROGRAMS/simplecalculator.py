def addition(num1,num2):
    sum=num1+num2
    return sum

def subtraction(num1,num2):
    sub=num1-num2
    return sub

def multiplication(num1,num2):
    multiply=num1*num2
    return multiply

def division(num1,num2):
    divide=num1//num2
    return divide

def modulus(num1,num2):
    mod=num1%num2
    return mod


num1=int(input("ENTER NUMBER 1:"))
num2=int(input("ENTER NUMBER 2:"))
    
sum=addition(num1,num2)
sub=subtraction(num1,num2)
multiply=multiplication(num1,num2)
divide=division(num1,num2)
mod=modulus(num1,num2)
    
print(f"SUM IS:{sum}\n")
print(f"SUBTRACTION IS:{sub}\n")
print(f"MULTIPLICATION IS:{multiply}\n")
print(f"DIVISION IS:{divide}\n")
print(f"MODULUS IS:{mod}\n")
    