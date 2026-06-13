#!/usr/bin/env python3
# Written by Joseph P.Vera
# 2024-11

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

data = np.loadtxt('graphene_bands.dat.gnu')

k = np.unique(data[:, 0])
bands1 = np.reshape(data[:, 1], (-1, len(k)))

EFermi = -1.7235
bands = bands1 - EFermi

fig, ax = plt.subplots(figsize=(6,5))

# Main plot
for band in range(len(bands)):
    ax.plot(k, bands[band, :], linewidth=1, color='xkcd:blue')

ax.set_xlim(min(k), max(k))
ax.set_ylim(-10, 5)

# Fermi energy
ax.axhline(0, linestyle='--', linewidth=0.75, color='xkcd:black')

# High symmetry k-points
ax.axvline(0.6667, linewidth=0.2, color='xkcd:black')
ax.axvline(1.0000, linewidth=0.2, color='xkcd:black')

ax.set_xticks([0, 0.6667, 1.0000, 1.5774])
ax.set_xticklabels([r'$\Gamma$', 'K', 'M', r'$\Gamma$'], fontsize=12)

ax.set_ylabel('Energy (eV)', fontsize=14)

# --------------------------------------------------
# Inset
# --------------------------------------------------
axins = ax.inset_axes([0.735, 0.55, 0.25, 0.25]) # [x, y, ancho, alto]
#axins = inset_axes(ax, width="25%", height="25%", loc="center right")

#ax.text(1.35, 2.05, r'~10$^{-6}$', fontsize=12)

for band in range(len(bands)):
    axins.plot(k, bands[band, :], linewidth=1, color='xkcd:blue')

# Zoomed region
axins.set_xlim(0.666699984, 0.666700014)
axins.set_ylim(-2e-7, 2e-7)
axins.ticklabel_format(axis='y', style='sci', scilimits=(-6, -6))

# Optional: remove tick labels
axins.tick_params(axis='both', which='both', bottom=False, top=False,
    left=True, right=False, labelbottom=False, labelleft=True)

# Draw box and connecting lines
mark_inset(ax, axins, loc1=2, loc2=3, fc="none", ec="black", lw=1)

plt.tight_layout()
plt.savefig("graphene.png", dpi=200, bbox_inches='tight')
#plt.show()
