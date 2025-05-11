def binary_search(arr, x, buffer=0):
    if len(arr) == 0:
        return -1

    mid = len(arr) // 2
    arr1, arr2 = arr[:mid], arr[mid + 1 :]

    if x == arr[mid]:
        return mid + buffer
    elif x < arr[mid]:
        return binary_search(arr1, x, buffer)
    else:
        return binary_search(arr2, x, buffer + mid + 1)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    x = arr[-1]
    print(binary_search(arr, x, 0))
