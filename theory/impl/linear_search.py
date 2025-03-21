def linear_search(A, x):
    for i in A:
        if i == x:
            return A.index(i)
        
    return -1 

A = [2, 3, 4]
print(linear_search(A, 4))
