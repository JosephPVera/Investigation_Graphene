import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('graphene_bands.dat.gnu')

k = np.unique(data[:, 0])
bands1 = np.reshape(data[:, 1], (-1, len(k)))

EFermi = -1.70715730
bands = bands1 - EFermi

#plt.figure(figsize=(12, 7))

for band in range(len(bands)):
    plt.plot(k, bands[band, :], linewidth=1, color='xkcd:blue') # , alpha=0.5
plt.xlim(min(k), max(k))

# Fermi energy
plt.axhline(0, linestyle='--', linewidth=0.75, color='xkcd:black')

# High symmetry k-points (check bands_pp.out)
plt.axvline(0.66666667, linewidth=0.2, color='xkcd:black')
plt.axvline(1.00000000, linewidth=0.2, color='xkcd:black')

# text labels
plt.xticks(ticks= [0, 0.66666667, 1.00000000, 1.57735027], labels=[r'$\Gamma$', 'K', 'M', r'$\Gamma$'], fontsize=12)

#plt.ylabel('Energy (eV)', fontsize=14)
plt.ylabel(r'Energy ($\mu$eV)', fontsize=14)
#plt.ylim(-10, 5)

plt.xlim(0.66666640, 0.66666694)
plt.ylim(-0.000035, 0.000035)


plt.gca().get_yaxis().get_offset_text().set_visible(False)
plt.ticklabel_format(axis='y', style='sci', scilimits=(-6, -6)) # 10^{-6}

plt.tight_layout()
plt.savefig("graphene.png", dpi=200, bbox_inches='tight')
#plt.show()
