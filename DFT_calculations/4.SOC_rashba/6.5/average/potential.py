import matplotlib.pyplot as plt
import numpy as np

# Load data
z, V = np.loadtxt('avg.dat', usecols=(0,1), unpack=True)

au2a = 0.529177249 # Convert a.u. to Angstrom
ry2ev = 13.605698066 # Convert Ry to eV


plt.plot(z*au2a, V*ry2ev, c='xkcd:blue')

#plt.plot(z*au2a, V, c='xkcd:blue')

# Plot a dashed line at zero
plt.axhline(-1.52391444, linestyle='--', linewidth=0.75, color='xkcd:black')

plt.xlim(0, 15)
plt.ylim(-40, 7)

#plt.ylim(-4, 4)

plt.xlabel('z ($\\AA$)', fontsize=14)
plt.ylabel(r'Energy ($V_{\mathrm{bare}} + V_{\mathrm{H}}$) (eV)', fontsize=14)

#plt.ylabel(r'Energy ($V_{\mathrm{bare}} + V_{\mathrm{H}}$) (Ry)', fontsize=14)

plt.tight_layout()
plt.savefig('potential.png', dpi=300)
