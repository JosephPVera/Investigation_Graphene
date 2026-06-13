#!/usr/bin/env python3
# Written by Joseph P.Vera
# 2026-06

import pyprocar

pyprocar.bandsplot(
    dirname=".",
    code="qe",
    mode="ipr",
    savefig = "ipr.png",
    fermi = -3.64471837,
    elimit = [-6.0, 6.0],
    knames=['Γ', 'X', 'Γ'],
    y_label_params={"fontsize": 14}
)
