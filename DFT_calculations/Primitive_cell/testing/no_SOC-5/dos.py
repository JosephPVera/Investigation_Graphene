#!/usr/bin/env python3
# Written by Joseph P.Vera
# 2024-11

import numpy as np
import matplotlib.pyplot as plt

EFermi =   -1.6797

# Load data, skipping the first line (header)
data = np.loadtxt('graphene_dos.dat', comments='#')

# Rescale energy
energy = data[:, 0] - EFermi

# DOS
dos = data[:, 1]

# Plot
plt.figure(figsize=(6,4))
plt.plot(energy, dos, color='xkcd:blue', linewidth=1)
plt.xlabel('Energy (eV) - EFermi')
plt.ylabel('DOS')
#plt.title('Density of States for Graphene (rescaled energy)')
#plt.grid(True)
#plt.ylim(0, 1)
plt.xlim(-3, 3)
plt.tight_layout()
plt.savefig("graphene_dos.png", dpi=300)
#plt.show()

