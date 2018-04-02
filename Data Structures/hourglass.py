arr = [[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]]

hourglass = [[1, 1, 1], [0, 1, 0], [1, 1, 1]]

col_index = 0
row_index = 0

max = -99999999

for i in range(len(arr)-2):
    for j in range(len(arr[i])-2):
        hourglassSum = arr[row_index][col_index] + arr[row_index][col_index+1] + arr[row_index][col_index+2] + arr[row_index+1][col_index+1] + arr[row_index+2][col_index] + arr[row_index+2][col_index+1] + arr[row_index+2][col_index+2]
        if hourglassSum > max:
            max = hourglassSum
        col_index = col_index+1
    col_index = 0
    row_index = row_index+1

print(max)
