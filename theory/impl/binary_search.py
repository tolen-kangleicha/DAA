def binary_search(A, x):
    beg, end = 0, len(A) - 1
    while beg <= end:
        mid = (beg + end) // 2
        if A[mid] == x:
            return mid 
        if A[mid] < x:
            beg = mid + 1
        else:
            end = mid - 1

    return -1 

A = [1, 2, 3, 4, 5]
print(binary_search(A, 3))

