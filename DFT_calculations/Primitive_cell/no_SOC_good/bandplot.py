import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('graphene_bands.dat.gnu')

k = np.unique(data[:, 0])
bands1 = np.reshape(data[:, 1], (-1, len(k)))

EFermi = -1.7237
bands = bands1 - EFermi

#plt.figure(figsize=(12, 7))

for band in range(len(bands)):
    plt.plot(k, bands[band, :], linewidth=1, color='xkcd:blue') # , alpha=0.5
plt.xlim(min(k), max(k))

# Fermi energy
plt.axhline(0, linestyle='--', linewidth=0.75, color='xkcd:black')

# High symmetry k-points (check bands_pp.out)
plt.axvline(0.6667, linewidth=0.2, color='xkcd:black')
plt.axvline(1.0000, linewidth=0.2, color='xkcd:black')

# text labels
plt.xticks(ticks= [0, 0.6667, 1.0000, 1.5774], labels=[r'$\Gamma$', 'K', 'M', r'$\Gamma$'], fontsize=12)
plt.ylabel("Energy (eV)", fontsize=14)
#plt.ylim(-20, 10)
#plt.ylim(-10, 5)

# check the cones -- 2 \mu eV
#plt.xlim(0.66669992, 0.66670007)
#plt.ylim(-0.000001, 0.000001)

# check new cones -- 0.4 \mu eV
plt.xlim(0.666699984, 0.666700014)
plt.ylim(-0.0000002, 0.0000002)

plt.tight_layout()
plt.savefig("graphene.png", dpi=200, bbox_inches='tight')
#plt.show()
