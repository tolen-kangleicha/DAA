x = [0] * 10


def n_queens(i, n):
    for j in range(1, n + 1):
        if place(i, j) == True:
            x[i] = j
            if i == n:
                print(x[1 : n + 1])
            else:
                n_queens(i + 1, n)


def place(i, j):
    for l in range(1, i):
        if x[l] == j or abs(l - i) == abs(x[l] - j):
            return False
    return True


print("For n = 4:")
n_queens(1, 4)
print("\nFor n = 5:")
n_queens(1, 5)
