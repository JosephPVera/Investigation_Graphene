#!/usr/bin/env python3
# Written by Joseph P.Vera
# 2024-11

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("grap_chg_2d.dat")

z = data.reshape((500, 500))

plt.imshow(z, origin='lower')
plt.colorbar(label='Charge density')
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.savefig("charge_density.png", dpi = 150)
#plt.show()
