"""Module to plot the different types of graph for some given functions"""

import math

import matplotlib.pyplot as plt
import numpy as np

# Define data
n = np.arange(1, 16)
log2n = np.log10(np.log2(n), where=np.log2(n) > 0)
nlog2n = np.log10(n * np.log2(n), where=np.log2(n) > 0)
n2 = np.log10(n**2)
n3 = np.log10(n**3)
n4 = np.log10(n**4)
twoN = np.log10(2**n)
nfact = np.log10([math.factorial(i) for i in n])

# Dictionary of functions
functions = {
    "log2(n)": log2n,
    "nlog2(n)": nlog2n,
    "n^2": n2,
    "n^3": n3,
    "n^4": n4,
    "2^n": twoN,
    "n!": nfact,
}

# Create a single figure with subplots
fig = plt.figure(figsize=(10, 6))

# Scatter plot
ax1 = plt.subplot(2, 2, 1)  # 2 rows, 2 columns, position 1
for name, values in functions.items():
    ax1.scatter(n, values, label=name)
ax1.legend()
ax1.set_xlabel("n")
ax1.set_ylabel("log10(f(n))")
ax1.set_title("Scatter Plot of log10 Growth Rates")
ax1.grid()

# Log-log plot
ax2 = plt.subplot(2, 2, 2)  # 2 rows, 2 columns, position 2
for name, values in functions.items():
    ax2.plot(np.log10(n), values, label=name)
ax2.legend()
ax2.set_xlabel("log10(n)")
ax2.set_ylabel("log10(f(n))")
ax2.set_title("Log-Log Plot of Growth Rates")
ax2.grid()

# Subplots for individual functions
ax3 = plt.subplot(2, 2, 3)  # 2 rows, 2 columns, position 3
for i, (name, values) in enumerate(functions.items()):
    ax3.plot(n, values, label=name)
ax3.legend()
ax3.set_xlabel("n")
ax3.set_ylabel("log10(f(n))")
ax3.set_title("Combined Plot of All Functions")
ax3.grid()

# Box plot
ax4 = plt.subplot(2, 2, 4)  # 2 rows, 2 columns, position 4
all_values = np.array(list(functions.values()))
ax4.boxplot(all_values.T, labels=functions.keys())
ax4.set_xlabel("Function")
ax4.set_ylabel("log10(f(n))")
ax4.set_title("Box Plot of log10 Growth Rates")
ax4.grid()

# Adjust layout and display
plt.tight_layout()
plt.show()
