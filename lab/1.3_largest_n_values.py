"""
Module to calculate the largest value of n for various time complexities given time limits.
"""

import math

# Constants for time limits in microseconds
TIME_LIMITS = {"1 second": 1e6, "1 minute": 60 * 1e6, "1 hour": 3600 * 1e6}


def lg_n(t):
    """Calculate the largest n such that log2(n) <= t."""
    exponent = (t / 1e6) * 1e6
    return f"2^{int(exponent):.2e}"


def sqrt_n(t):
    """Calculate the square root of t."""
    return round(t**0.5, 2)


def linear_n(t):
    """Calculate the largest n such that n <= t."""
    return round(t, 2)


def n_lg_n(t):
    """Calculate the largest n such that n * log2(n) <= t."""
    n = 1
    while n * math.log2(n) <= t:
        n += 1
    return n - 1


def n_squared(t):
    """Calculate the largest n such that n^2 <= t."""
    return int(math.sqrt(t))


def n_cubed(t):
    """Calculate the largest n such that n^3 <= t."""
    return int(t ** (1 / 3))


def two_power_n(t):
    """Calculate the largest n such that 2^n <= t."""
    n = 1
    while 2**n <= t:
        n += 1
    return n - 1


def factorial_n(t):
    """Calculate the largest n such that n! <= t."""
    n = 1
    fact = 1
    while fact <= t:
        n += 1
        fact *= n
    return n - 1


# Dictionary of functions to compute n for different time complexities
FUNCTIONS = {
    "lg n": lg_n,
    "√n": sqrt_n,
    "n": linear_n,
    "nlogn": n_lg_n,
    "n^2": n_squared,
    "n^3": n_cubed,
    "2^n": two_power_n,
    "n!": factorial_n,
}

# Compute results for each function and time limit
results = []
for func_label, func in FUNCTIONS.items():
    row = []
    for time_label, time_value in TIME_LIMITS.items():
        row.append(func(time_value))
    results.append(row)

# Define headers and row labels
headers = ["", "1 second", "1 minute", "1 hour"]
row_labels = list(FUNCTIONS.keys())


def format_value(value):
    """Format the value for display in the table."""
    if isinstance(value, str):
        return f"{value:<15}"
    if value < 1e2:
        return f"{value:<15.2f}"
    return f"{value:<15.2e}"


# Print the table
HEADER_ROW = "".join(f"{header:<15}" for header in headers)
print(HEADER_ROW)
print("-" * len(HEADER_ROW))

for i, func_label in enumerate(FUNCTIONS):
    row = [f"{func_label:<15}"] + [
        format_value(results[i][j]) for j in range(len(TIME_LIMITS))
    ]
    print("".join(row))
