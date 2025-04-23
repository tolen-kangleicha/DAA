n = 4
x = [0] * (n + 1)


def n_queens(i):
    for j in range(1, n + 1):
        if place(i, j) == True:
            x[i] = j
            if i == n:
                print(x[1 : n + 1])
            else:
                n_queens(i + 1)


def place(i, j):
    for l in range(1, i):
        if x[l] == j or abs(l - i) == abs(x[l] - j):
            return False
    return True


n_queens(1)
