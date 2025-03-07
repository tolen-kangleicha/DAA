"""
Module to find the minimum element in a list of n elements using DNC algorithm.
"""

import random
import time

import matplotlib.pyplot as plt


# Modified Divide-and-Conquer algorithm to find the minimum
def find_min_dnc(arr, comparison_count=0):
    """
    Method to find the minimum value and count comparisons.
    """
    if len(arr) == 1:  # Base case
        return arr[0], comparison_count
    mid = len(arr) // 2  # Find midpoint
    l1 = arr[:mid]  # Left sublist
    l2 = arr[mid:]  # Right sublist
    min1, comparison_count = find_min_dnc(l1, comparison_count)  # Recursive call on L1
    min2, comparison_count = find_min_dnc(l2, comparison_count)  # Recursive call on L2

    comparison_count += 1  # Count the comparison
    return (min1 if min1 < min2 else min2), comparison_count  # Combine results


# Main script
n_values = [10, 100, 1000, 10_000, 100_000]
e_values = []
t_values = []

for n in n_values:
    ran_list = [random.randint(1, 1_000_000) for _ in range(n)]  # Generate random list
    start_time = time.perf_counter()
    min_value, comparisons = find_min_dnc(ran_list)  # Find the minimum element
    end_time = time.perf_counter()
    e_values.append(comparisons)  # Total comparisons
    t_values.append((end_time - start_time) * 1_000)  # Time in microseconds

# Printing the table
print("n\t", "\t".join(map(str, n_values)))
print("e\t", "\t".join(map(str, e_values)))
print("t\t", "\t".join(f"{t:.2f}" for t in t_values))

# Plotting results
plt.figure(figsize=(10, 6))

# Graph 1: Comparisons
plt.subplot(1, 2, 1)
plt.plot(n_values, e_values, marker="o", label="Comparisons (e)")
plt.xlabel("Input Size (n)")
plt.ylabel("Number of Comparisons (e)")
plt.title("Comparisons vs Input Size")
plt.grid(True)
plt.legend()

# Graph 2: Time Taken
plt.subplot(1, 2, 2)
plt.plot(n_values, t_values, marker="o", color="r", label="Time Taken (t)")
plt.xlabel("Input Size (n)")
plt.ylabel("Time Taken (μs)")
plt.title("Time Taken vs Input Size")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
