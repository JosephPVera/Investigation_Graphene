#!/usr/bin/env python3
# Written by Joseph P.Vera
# 2024-11

import matplotlib.pyplot as plt
import numpy as np

# === Ajustes ===
EFermi = -1.70715730

# === Función para cargar datos ===
def load_pdos(fname, EFermi):
    """
    Carga un archivo PDOS de Quantum ESPRESSO.
    Detecta automáticamente si contiene proyecciones SOC (múltiples columnas)
    y devuelve energía (alineada al EF) y la PDOS total de ese orbital.
    """
    data = np.loadtxt(fname)
    energy = data[:, 0] - EFermi
    ncols = data.shape[1]

    # Manejo automático del número de columnas
    if ncols >= 3:
        # Sumar todas las columnas de proyección parciales (desde la 3ª en adelante)
        pdos = np.sum(data[:, 2:], axis=1)
    else:
        raise ValueError(f"Formato inesperado en {fname}: {ncols} columnas")

    return energy, pdos


# === Cargar archivos ===
energy, pdos_s = load_pdos("graphene_pdos.dat.pdos_atm#1(C)_wfc#1(s_j0.5)", EFermi)
_, pdos_pj05 = load_pdos("graphene_pdos.dat.pdos_atm#1(C)_wfc#2(p_j0.5)", EFermi)
_, pdos_pj15 = load_pdos("graphene_pdos.dat.pdos_atm#1(C)_wfc#3(p_j1.5)", EFermi)

# Combinar contribuciones p (j=0.5 + j=1.5)
pdos_p_total = pdos_pj05 + pdos_pj15


# === Gráfica ===
#plt.figure(figsize=(8, 4))

plt.plot(energy, pdos_s, linewidth=1, color='xkcd:green', label='s (j=0.5)')
plt.plot(energy, pdos_pj05, linewidth=1, color='xkcd:blue', label='p (j=0.5)')
plt.plot(energy, pdos_pj15, linewidth=1, color='xkcd:red', label='p (j=1.5)')
#plt.plot(energy, pdos_p_total, linewidth=1.2, color='xkcd:dark blue', label='p total')

plt.xlabel('Energy (eV)', fontsize=14)
plt.ylabel('DOS (States/eV)', fontsize=14)
plt.axvline(x=0, color='black', linestyle='--', linewidth=0.8)

plt.xlim(-20, 15)
plt.ylim(0, 0.4)

plt.legend()
plt.tight_layout()
plt.savefig("graphene_pdos_SOC-atomo_1.png", dpi=300)
#plt.show()
