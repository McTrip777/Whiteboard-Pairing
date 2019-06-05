inputMatrix = [
    [0,  1,  2,  3,  4],
    [13, 14, 15, 16, 5],
    [12, 19, 18, 17, 6],
    [11, 10, 9,  8,  7]
]

def spiral(arr): 
    orderArr = []
    newOrderArr = []
    temp = []
    for h in range(0, len(arr[0])):                         #left to right [0][0, h]
        orderArr.append(arr[0][h])
    for i in range(1, len(arr)):                            # top to bottom [1, i][4]
        for j in range(0, len(arr[i])):
            if arr[i][j] == arr[i][len(arr[i])-1]:
                orderArr.append(arr[i][j])
            else:
                continue
    for k in reversed(range(0, len(arr[len(arr) -1])-1)):   # right to left [3][0, k-1] reversed
        orderArr.append(arr[len(arr) -1][k])
    for l in reversed(range(1, len(arr)-1)):                # bottom to top [0, l-1][0] reversed
        for m in range(0, len(arr[l])):
            if arr[l][m] == arr[l][0]:
                orderArr.append(arr[l][m])
            else:
                continue


    for n in range(1, len(arr[0])-1):                       #left to right [1][1, h-1]
        orderArr.append(arr[1][n])
    for o in range(2, len(arr)-1):                          # top to bottom [2, i-1][3]
        for p in range(0, len(arr[o])):
            if arr[o][p] == arr[o][len(arr[o])-2]:
                orderArr.append(arr[o][p])
            else:
                continue
    for p in reversed(range(1, len(arr[len(arr) -2])-2)):   # right to left [2][1, k-2] reversed
        orderArr.append(arr[len(arr) -2][p])
    return orderArr 




print(spiral(inputMatrix))