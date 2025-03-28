import random
import time

import matplotlib.pyplot as plt


# Function to generate a list of n random numbers
def generate_list(n):
    return [random.randint(1, 100000) for _ in range(n)]


# Divide-and-Conquer Search Algorithm
def dac_search(x, L):
    comparisons = 1
    if len(L) == 1:
        if L[0] == x:
            return 0, comparisons
        else:
            return -1, comparisons
    mid = len(L) // 2
    L1, L2 = L[:mid], L[mid:]
    i, c1 = dac_search(x, L1)
    comparisons += c1
    if i != -1:
        return i, comparisons
    j, c2 = dac_search(x, L2)
    comparisons += c2
    if j != -1:
        return mid + j, comparisons
    return -1, comparisons


# Function to measure time and comparisons
def measure_performance(A, x):
    start_time = time.time()
    index, comparisons = dac_search(x, A)
    end_time = time.time()
    return comparisons, (end_time - start_time) * 1000  # Convert to milliseconds


# Main function to run the experiments
def run_experiments():
    sizes = [10, 100, 1000, 10000]
    results = {
        "e_first": [],
        "e_last": [],
        "e_not_found": [],
        "t_first": [],
        "t_last": [],
        "t_not_found": [],
    }

    for n in sizes:
        A = generate_list(n)

        # Case 1: x is the first element
        e_first, t_first = measure_performance(A, A[0])
        results["e_first"].append(e_first)
        results["t_first"].append(t_first)

        # Case 2: x is the last element
        e_last, t_last = measure_performance(A, A[-1])
        results["e_last"].append(e_last)
        results["t_last"].append(t_last)

        # Case 3: x is not in the list
        e_not_found, t_not_found = measure_performance(A, -1)
        results["e_not_found"].append(e_not_found)
        results["t_not_found"].append(t_not_found)

    return results, sizes


# Function to plot results
def plot_results(results, sizes):
    plt.figure(figsize=(12, 6))

    # Plot comparisons
    plt.subplot(1, 2, 1)
    plt.plot(sizes, results["e_first"], label="First Element")
    plt.plot(sizes, results["e_last"], label="Last Element")
    plt.plot(sizes, results["e_not_found"], label="Not Found")
    plt.xlabel("List Size (n)")
    plt.ylabel("Comparisons (e)")
    plt.title("Divide-and-Conquer Search - Comparisons")
    plt.legend()
    plt.grid()

    # Plot time
    plt.subplot(1, 2, 2)
    plt.plot(sizes, results["t_first"], label="First Element")
    plt.plot(sizes, results["t_last"], label="Last Element")
    plt.plot(sizes, results["t_not_found"], label="Not Found")
    plt.xlabel("List Size (n)")
    plt.ylabel("Time (ms)")
    plt.title("Divide-and-Conquer Search - Time")
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()


# Run experiments and plot results
results, sizes = run_experiments()
plot_results(results, sizes)

# Print results in table format
print("Divide-and-Conquer Search Results")
print(f"{'n':<10}{'e_first':<15}{'e_last':<15}{'e_not_found':<15}")
for i, n in enumerate(sizes):
    print(
        f"{n:<10}{results['e_first'][i]:<15}{results['e_last'][i]:<15}{results['e_not_found'][i]:<15}"
    )

print(f"\n{'n':<10}{'t_first':<15}{'t_last':<15}{'t_not_found':<15}")
for i, n in enumerate(sizes):
    print(
        f"{n:<10}{results['t_first'][i]:<15.4f}{results['t_last'][i]:<15.4f}{results['t_not_found'][i]:<15.4f}"
    )
