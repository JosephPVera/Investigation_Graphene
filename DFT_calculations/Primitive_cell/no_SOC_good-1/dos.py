#!/usr/bin/env python3
# Written by Joseph P.Vera
# 2024-11

import numpy as np
import matplotlib.pyplot as plt

EFermi =   -1.7237

# Load data, skipping the first line (header)
data = np.loadtxt('graphene_dos.dat', comments='#')

# Rescale energy
energy = data[:, 0] - EFermi

# DOS
dos = data[:, 1]

# Plot
plt.figure(figsize=(12,7)) # (6,4)
plt.plot(energy, dos, color='xkcd:blue', linewidth=1)
plt.axvline(x=0, color='xkcd:black', linestyle='--', linewidth=1) # Fermi energy
plt.xlabel('Energy (eV)', fontsize=16)
plt.ylabel('DOS (States/eV)', fontsize=16)
#plt.title('Density of States for Graphene (rescaled energy)')
#plt.grid(True)
#plt.ylim(0, 0.9)
#plt.xlim(-2.5, 2)
plt.xlim(-20, 15)
plt.ylim(0, 1.85)
plt.tight_layout()
plt.savefig("graphene_dos.png", dpi=300)
#plt.show()

