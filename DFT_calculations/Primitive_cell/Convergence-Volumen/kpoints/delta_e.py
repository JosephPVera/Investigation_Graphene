#!/usr/bin/env python3
# Written by Joseph P.Vera
# 2024-11

import numpy as np
import matplotlib.pyplot as plt

# Load the file (skip the header line with column names)
data = np.loadtxt("delta_e.dat", skiprows=1)

# Extract columns
ENCUT = data[:, 0]
delta_e = data[:, 2]

# Plot
plt.figure(figsize=(8,6))
plt.plot(ENCUT, delta_e, marker='o', color="xkcd:red")

plt.xlabel("K-point mesh", fontsize=12)
plt.ylabel("Relative energy (Ry)", fontsize=12)
plt.title("Relative Energy vs K-point", fontsize=14)
#plt.legend()
#plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("delta_e_kpoint.png", dpi=150)
#plt.show()

