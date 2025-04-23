def subset_sum_all(arr, n, target, subset=[], all_solutions=[]):
    if target == 0:
        all_solutions.append(subset)
        return

    if n == 0 or target < 0:
        return

    # Include current element
    subset_sum_all(
        arr, n - 1, target - arr[n - 1], subset + [arr[n - 1]], all_solutions
    )

    # Exclude current element
    subset_sum_all(arr, n - 1, target, subset, all_solutions)


# Example usage
arr = [3, 34, 4, 12, 5, 2]
target = 9
solutions = []
subset_sum_all(arr, len(arr), target, [], solutions)

if solutions:
    print("All subsets summing to", target, "are:")
    for s in solutions:
        print(s)
else:
    print("No subsets found.")
