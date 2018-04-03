arr = [1,2,3,4,5]
r = 1

for i in range(0, r):
    arr.append(arr[0])
    arr.pop(0)

print(arr)
