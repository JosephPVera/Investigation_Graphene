import matplotlib.pyplot as plt
import numpy as np

# Load data
z, V = np.loadtxt('avg.dat', usecols=(0,1), unpack=True)

au2a = 0.529177249 # Convert a.u. to Angstrom
ry2ev = 13.605698066 # Convert Ry to eV


plt.plot(z*au2a, V*ry2ev, c='b')

# Plot a dashed line at zero
plt.axhline(0, c='gray', ls='--')

plt.xlim(0, 15)
plt.ylim(-40, 10)

plt.xlabel('z ($\\AA$)')
plt.ylabel('Electrostatic potential (eV)')

plt.savefig('potential.png', dpi=300)
