def is_sorted(A):
    asc, desc = True, True
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            asc = False
        else:
            desc = False
    return asc or desc

A = [1, 2, 3]
print(is_sorted(A))
