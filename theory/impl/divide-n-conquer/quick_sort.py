import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    arr = [random.randint(0, 100) for _ in range(10)]
    print("Random array:", arr)
    print("Sorted array:", quick_sort(arr))
