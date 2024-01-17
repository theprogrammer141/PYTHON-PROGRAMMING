x=int(input("ENTER VALUE OF X:"))

match x:
    case 0:
        print("X IS ZERO")
    case 4:
        print("X IS 4")
    case _:
        print(x)