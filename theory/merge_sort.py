"""
def merge_sort(A, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(A, low, mid)
        merge_sort(A, mid + 1, high)
        merge(A, low, mid, high)  

def merge(A, low, mid, high):
    i, j = low, mid + 1
    B = []

    # Merge the two halves into B
    while i <= mid and j <= high:
        if A[i] < A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1

    # Copy remaining elements from the first half
    while i <= mid:
        B.append(A[i])
        i += 1

    # Copy remaining elements from the second half
    while j <= high:
        B.append(A[j])
        j += 1

    # Copy back sorted elements to A
    for k in range(len(B)):
        A[low + k] = B[k]

if __name__ == "__main__":
    A = [3, 2, 20, 1, 49]
    print("Original:", A)
    merge_sort(A, 0, len(A) - 1)
    print("Sorted:", A)
"""

def merge_sort(arg):
    """Method to sort a list of elements using merge_sort algo that uses the technique of DNC"""
    if len(arg) > 1:
        # Find the middle point and divide the array into two halves
        mid = len(arg) // 2
        left_half = arg[:mid]
        right_half = arg[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Initialize pointers for left_half, right_half, and the main array
        i = j = k = 0

        # Merge the sorted halves back into the main array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any elements were left in the left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check if any elements were left in the right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)
