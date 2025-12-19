#!/usr/bin/env python3
# Written by Joseph P.Vera
# 2024-10

import sys
import getopt
import matplotlib
import matplotlib.pyplot as plt

from pymatgen.io.vasp import BSVasprun
from pymatgen.electronic_structure.plotter import BSPlotter

# =========================
# Opciones por defecto
# =========================
vasprunfile = "vasprun.xml"
backend = False
noshow = False

# =========================
# Opciones CLI
# =========================
shopts = "hf:bn"
longopts = ["help", "file=", "backend", "noshow"]

opts, args = getopt.getopt(sys.argv[1:], shopts, longopts)

for o, a in opts:
    if o in ("-h", "--help"):
        print("Usage: band.py [-f vasprun.xml]")
        sys.exit()
    elif o in ("-f", "--file"):
        vasprunfile = a
    elif o in ("-b", "--backend"):
        backend = True
    elif o in ("-n", "--noshow"):
        noshow = True

if backend:
    matplotlib.use("tkagg")

# =========================
# Leer VASP
# =========================
v = BSVasprun(vasprunfile)
bs = v.get_band_structure(
    kpoints_filename="KPOINTS",
    line_mode=True
)

# =========================
# Plot
# =========================
plotter = BSPlotter(bs)
plot = plotter.get_plot(
    zero_to_efermi=True,
    ylim= (-0.0000002, 0.0000002) 
    #ylim= (-10,5) 
)

# =========================
# Compatibilidad total
# =========================
if hasattr(plot, "set_xlim"):      # Axes
    ax = plot
    fig = ax.figure
else:                              # Figure
    fig = plot
    ax = fig.axes[0]

# =========================
# CAMBIAR COLOR DE LAS BANDAS
# =========================
for line in ax.lines:
    xdata = line.get_xdata()

    # Líneas verticales = puntos de alta simetría
    if len(xdata) == 2 and xdata[0] == xdata[1]:
        line.set_color('xkcd:black')
        line.set_linewidth(0.2)
    else:
        # Bandas electrónicas
        line.set_color('xkcd:blue')
        line.set_linewidth(1)

# =========================
# Ajustes finales
# =========================
print("xticks:", ax.get_xticks())
print("xlim:", ax.get_xlim())

ax.set_xlim(1.712581427, 1.712581505) 
#ax.set_ylabel("Energía (eV)", fontsize=16)
plt.ylabel(r'Energía ($\mu$eV)', fontsize=16)

ax.set_xlabel("")
ax.axhline(0.0, linestyle="--", linewidth=0.75, color='xkcd:black')

ax.tick_params(axis='x', labelsize=12)   # tamaño del texto Γ, X, M, etc.
ax.tick_params(axis='y', labelsize=12)

leg = ax.get_legend()
if leg is not None:
    leg.remove()
    
plt.gca().get_yaxis().get_offset_text().set_visible(False)
plt.ticklabel_format(axis='y', style='sci', scilimits=(-6, -6)) # 10^{-6}

fig.set_size_inches(6.4, 4.8)
plt.tight_layout()
fig.savefig("bandstruct.png", dpi=200, bbox_inches='tight')

#if not noshow:
#    plt.show()


