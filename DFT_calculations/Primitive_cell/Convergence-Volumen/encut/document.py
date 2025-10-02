#!/usr/bin/env python3
# Written by Joseph P.Vera
# 2024-11

import numpy as np
import matplotlib.pyplot as plt

# Load the file (skip the header line with column names)
data = np.loadtxt("information.dat", skiprows=1)

# Extract columns
ENCUT = data[:, 0]
Pristine = data[:, 1]
Increased = data[:, 2]
Decreased = data[:, 3]

# Compute relative energies
rel_increased = np.abs(Increased - Pristine)
rel_decreased = np.abs(Decreased - Pristine)

# Plot
plt.figure(figsize=(8,6))
plt.plot(ENCUT, rel_increased, marker='o', label='|Increased - Pristine|', color="xkcd:blue")
plt.plot(ENCUT, rel_decreased, marker='s', label='|Decreased - Pristine|', color="xkcd:red")

plt.xlabel("ENCUT (Ry)", fontsize=12)
plt.ylabel("Relative energy (Ry)", fontsize=12)
plt.title("Relative Energy vs ENCUT", fontsize=14)
plt.legend()
#plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("convergence_encut.png", dpi=150)
#plt.show()

