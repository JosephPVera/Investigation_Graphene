#!/usr/bin/env python3
# Written by Joseph P.Vera
# 2024-11

import numpy as np
import matplotlib.pyplot as plt

# Load the file (skip the header line with column names)
data = np.loadtxt("gap.dat", skiprows=1)

# Extract columns
field = data[:, 0]
gap = data[:, 1]

# Plot
#plt.figure(figsize=(8,6))
plt.plot(field, gap, marker='o', color="xkcd:blue")

plt.xlabel("External Electric Field (V/nm)", fontsize=14)
plt.ylabel("Band Gap (µeV)", fontsize=14)
#plt.title("Relative Energy vs ENCUT", fontsize=14)
#plt.legend()
#plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("gap.png", dpi=150)
#plt.show()

