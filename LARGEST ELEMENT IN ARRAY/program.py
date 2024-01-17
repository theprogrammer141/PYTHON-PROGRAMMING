arr=[10,20,30]
max=arr[0]
for i in range(1,len(arr)):
    if(max<arr[i]):
        max=arr[i]

print(max)