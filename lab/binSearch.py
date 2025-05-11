count = 0
depth = 0


def binSearch(arr, x, offset=0):
    global count
    global depth
    if len(arr) == 0:
        return -1, count, depth
    mid = len(arr) // 2
    count += 1
    depth += 1
    if x == arr[mid]:
        return offset + mid, count, depth
    elif x > arr[mid]:
        return binSearch(arr[mid + 1 :], x, offset + mid + 1)
    else:
        return binSearch(arr[:mid], x, offset)


arr = [1, 2, 3, 4, 5, 6, 9]
x = arr[-1]
print(binSearch(arr, x))
