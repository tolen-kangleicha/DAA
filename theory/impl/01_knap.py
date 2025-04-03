def knap(i, p, w, m):
    if m < 0:
        return float('-inf')
    if i < 0:
        return 0
    val1 = knap(i-1, p, w, m)
    val2 = p[i] + knap(i-1, p, w, m-w[i])
    return max(val1, val2)

print(knap(2, [10, 20, 15], [3, 4, 7], 7))
