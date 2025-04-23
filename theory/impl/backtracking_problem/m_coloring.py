x = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m = 3


def colorable(k, i):
    for j in range(1, k - 1):
        if adj(j - k) == True and x[j] == i:
            return False
    return True


def m_color(k, n, m):
    for i in range(1, m):
        if colorable(k, i) == True:
            x[k] = i
            if k == n:
                print(x[1:n])
            else:
                m_color(k + 1, n, m)
