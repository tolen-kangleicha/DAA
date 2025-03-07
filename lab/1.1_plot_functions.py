""""Module to plot the line & bar graph for some given functions."""

import math

import matplotlib.pyplot as plt
import numpy as np

# Generate x-axis values (n from 1 to 15)
n = np.arange(1, 16)

# Define the functions and compute their logarithmic values (base 10)
log2n = np.log10(np.log2(n))
nlog2n = np.log10(n * np.log2(n))
n2 = np.log10(n**2)
n3 = np.log10(n**3)
n4 = np.log10(n**4)
twoN = np.log10(2**n)
nfact = np.log10([math.factorial(i) for i in n])

# Store functions in a dictionary
functions = {
    "log2(n)": log2n,
    "nlog2(n)": nlog2n,
    "n^2": n2,
    "n^3": n3,
    "n^4": n4,
    "2^n": twoN,
    "n!": nfact,
}

# Plotting the graphs
plt.figure(figsize=(15, 8))

# Plot line graphs
for name, values in functions.items():
    plt.plot(n, values, label=f"{name} (line)")

# Plot bar graphs
BAR_WIDTH = 0.1  # Set a non-zero width for bars
offsets = np.arange(len(functions)) * BAR_WIDTH  # Adjust offsets for each function
for i, (name, values) in enumerate(functions.items()):
    plt.bar(n + offsets[i], values, width=BAR_WIDTH, label=f"{name} (bar)")

# Add labels, title, and legend
plt.xlabel("n")
plt.ylabel("log10(f(n))")
plt.title("Comparison of Growth Rates of Functions")
plt.legend()
plt.grid()
plt.show()
