def knap(ind, MaxCap):
    if MaxCap < 0:
        return float("-inf")
    if ind < 0:
        return 0
    val1 = knap(ind - 1, MaxCap)
    val2 = Profits[ind] + knap(ind - 1, MaxCap - Weights[ind])
    return max(val1, val2)


if __name__ == "__main__":
    Profits = [10, 20, 15]
    Weights = [3, 4, 7]
    print(knap(len(Profits) - 1, 7))
