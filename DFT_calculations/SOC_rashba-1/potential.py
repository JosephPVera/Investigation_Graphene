import matplotlib.pyplot as plt
plt.style.use('../../matplotlib/sci.mplstyle')
import numpy as np

# Load data
z, V = np.loadtxt('avg.dat', usecols=(0,1), unpack=True)

au2a = 0.529177249 # Convert a.u. to Angstrom
ry2ev = 13.605698066 # Convert Ry to eV

# Create figure object
plt.figure(figsize=(4.5,4.5))
# Plot the data, using blue color
plt.plot(z*au2a, V*ry2ev, c='b')
# Plot a dashed line at zero
plt.axhline(0, c='gray', ls='--')
# Set the axis limits
plt.xlim(0, 20)
plt.ylim(-40, 10)
# Add the x and y-axis labels
plt.xlabel('z ($\AA$)')
plt.ylabel('Electrostatic potential (Ry)')
# Save a figure to the pdf file
plt.savefig('plot-V.pdf')
# Show figure
plt.show()
