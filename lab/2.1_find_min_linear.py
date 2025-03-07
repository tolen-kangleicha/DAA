"""
Module to find the minimum element in a list and measure the time taken.
"""

import random
import time

import matplotlib.pyplot as plt


# Function to find the minimum element and count comparisons
def find_min_and_measure_time(input_list):
    """
    Finds the minimum element in a list and measures the time taken.

    Args:
        input_list (list): The list of integers to search.

    Returns:
        tuple: A tuple containing the minimum element, number of comparisons,
        and time taken in milliseconds.
    """
    comparisons = 0
    minimum = float("inf")
    start_time = time.perf_counter()

    for elem in input_list:
        comparisons += 1  # Count the comparison
        minimum = min(minimum, elem)
    end_time = time.perf_counter()
    time_taken = (end_time - start_time) * 1000  # Convert to ms
    return minimum, comparisons, time_taken


# Main script
if __name__ == "__main__":
    n_values = [10, 100, 1000, 10_000, 100_000]
    c_values = []
    t_values = []

    for n in n_values:
        random_list = [
            random.randint(1, 1_000_000) for _ in range(n)
        ]  # Generate random list
        _, c, t = find_min_and_measure_time(random_list)
        c_values.append(c)
        t_values.append(t)

    # Printing the table
    print("n\t", "\t".join(map(str, n_values)))
    print("c\t", "\t".join(map(str, c_values)))
    print("t\t", "\t".join(f"{t:.3f}" for t in t_values))

    # Plotting
    plt.figure(figsize=(10, 6))
    # Graph 1: Comparisons
    plt.subplot(1, 2, 1)
    plt.plot(n_values, c_values, marker="o", label="Comparisons")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Number of Comparisons (c)")
    plt.title("Comparisons vs Input Size")
    plt.grid(True)
    plt.legend()

    # Graph 2: Time Taken
    plt.subplot(1, 2, 2)
    plt.plot(n_values, t_values, marker="s", color="r", label="Time Taken")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time Taken (ms)")
    plt.title("Time Taken vs Input Size")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()
