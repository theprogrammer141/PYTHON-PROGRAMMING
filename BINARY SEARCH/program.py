def sort_in_ascending(arr):
    temp = 0
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    print("SORTED LIST:")
    for i in range(0, len(arr)):
        print(arr[i])


def binary_search(arr):
    left = 0
    right = len(arr)-1
    mid = 0
    sort_in_ascending(arr)
    value = int(input("ENTER VALUE TO BE SEARCHED:"))
    while left <= right:
        mid = int(left+right/2)
        if value == arr[mid]:
            return mid
        elif value < arr[mid]:
            right = mid-1
        else:
            left = mid+1

    return -1


lt = [10, 34, 32, 98, 76, 56]
result = binary_search(lt)
if result != -1:
    print("ELEMENT FOUND AT INDEX:", result)
else:
    print("ELEMENT NOT FOUND!")
