import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('ZGNR_bands.dat.gnu')

k = np.unique(data[:, 0])
bands1 = np.reshape(data[:, 1], (-1, len(k)))

EFermi = -3.76362789
bands = bands1 - EFermi

for band in range(len(bands)):
    plt.plot(k, bands[band, :], linewidth=1, color='xkcd:blue') # , alpha=0.5
plt.xlim(min(k), max(k))

# Fermi energy
plt.axhline(0, linestyle='--', linewidth=0.75, color='xkcd:black')

# High symmetry k-points (check bands_pp.out)
plt.axvline(0.500000, linewidth=0.2, color='xkcd:black')

# text labels
plt.xticks(ticks= [0, 0.500000, 1.0000], labels=[r'$\Gamma$', 'X', r'$\Gamma$'], fontsize=12)

plt.ylabel('Energy (eV)', fontsize=14)
plt.ylim(-6, 6)

plt.tight_layout()
plt.savefig("graphene.png", dpi=200, bbox_inches='tight')
