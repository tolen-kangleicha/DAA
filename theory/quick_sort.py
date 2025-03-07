"""
Module to demonstrate the technique of quick sort algorithm that uses the technique of divide and conquer

def partition(arr, low, high):
    pivot, i, j = arr[low], low + 1, high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

if __name__ == "__main__":
    arr_list = [40, 20, 80, 70, 30]
    quick_sort(arr_list, 0, len(arr_list) - 1)
    print("Sorted array:", arr_list)
"""


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:

        pivot = arr[0]
        left = [i for i in arr[1:] if i <= pivot]
        right = [i for i in arr[1:] if i > pivot]
        return quick_sort(left) + pivot + quick_sort(right)


print(quick_sort([3, 2, 5, 4, 1]))
