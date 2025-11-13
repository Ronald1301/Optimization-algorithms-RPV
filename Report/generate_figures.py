"""
Genera figuras usadas en el informe `optimization_report.tex`.
Crea `Report/placeholder_robustez.png` (sobrescribe si existe) y una figura de ejemplo en ../figures/.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

HERE = Path(__file__).parent
ROOT = HERE.parent
FIGURES_DIR = ROOT / 'figures'
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# Generar placeholder_robustez.png
x = np.linspace(0, 120, 200)
y_gd = 50 * np.exp(-0.03 * x) + 5

y_newton = 15 * np.exp(-0.05 * x) + 2

y_hybrid = 30 * np.exp(-0.04 * x) + 3

plt.figure(figsize=(6,4))
plt.semilogy(x, y_gd, label='GD Adaptivo')
plt.semilogy(x, y_newton, label='Newton')
plt.semilogy(x, y_hybrid, label='Híbrido')
plt.xlabel('Distancia inicial')
plt.ylabel('Iteraciones (simulado)')
plt.title('Robustez vs Distancia inicial (placeholder)')
plt.legend()
plt.grid(True, which='both', alpha=0.3)

out = HERE / 'placeholder_robustez.png'
plt.savefig(out, dpi=150)
print(f"Wrote {out}")

# Copiar figura a ../figures como ejemplo
fig_example = FIGURES_DIR / 'robustez_example.png'
plt.savefig(fig_example, dpi=150)
print(f"Wrote {fig_example}")
