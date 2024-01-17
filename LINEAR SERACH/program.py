key = int(input("ENTER NUMBER TO SEARCH:"))
flag = 0
arr = [10, 20, 30, 40, 50]
for i in range(0, len(arr)):
    if key == arr[i]:
        print("ELEMENT FOUND AT INDEX", i)
        flag = 1
        break

if flag == 0:
    print("ELEMENT NOT FOUND")
    print("\n")
