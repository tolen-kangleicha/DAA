def linear_search(A, x):
    for num in A:
        if num == x:
            return A.index(num)

    return -1


if __name__ == "__main__":
    A = [2, 3, 4]
    print(linear_search(A, 4))
