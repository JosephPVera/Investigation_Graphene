#!/usr/bin/env python3
# Written by Joseph P.Vera
# 2024-11

import matplotlib.pyplot as plt
import numpy as np

# Load data, skipping the header (line starting with #)
data = np.loadtxt("information.dat", comments="#")

# Split into columns
encut = data[:, 0]   # First column = ENCUT
energy = data[:, 1]  # Second column = Total energy

# Plot
plt.figure(figsize=(7,5))
plt.plot(encut, energy, marker="o", linestyle="-", color="b", label="Total Energy")

# Labels and title
plt.xlabel("ENCUT (Ry)", fontsize=12)
plt.ylabel("Total Energy (Ry)", fontsize=12)
plt.title("ENCUT vs Total Energy", fontsize=14)

# Grid and legend
#plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Show the plot
plt.tight_layout()
plt.savefig("convergence_encut.png", dpi=150)
#plt.show()

