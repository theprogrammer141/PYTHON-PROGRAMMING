while True:
    sales=float(input("ENTER SALES IN POUNDS(-1 TO END):"))

    if sales==-1:
        break

    base_salary=200.00
    commission_rate=0.09
    salary=base_salary+(sales * commission_rate)

    print("SALARY IS:",format(salary,".2f"))
