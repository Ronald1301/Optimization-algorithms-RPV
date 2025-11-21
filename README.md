 # Proyecto: Análisis de Optimización

Este repositorio contiene notebook y recursos para el análisis numérico de la función
f(x,y) = log(x^2 + y^2 + 1) * arctan(x^2 + y^2) y experimentación con distintos algoritmos de
optimización (Gradiente, Newton, Quasi-Newton, Trust-Region, métodos de penalidad, etc.).

Contenido principal
- `notebooks/optimization_analysis.ipynb` : notebook con definiciones, análisis teórico,
   implementaciones y experimentos reproducibles.
- `Report/` : archivos relacionados con el informe LaTeX (`optimization_report.tex`, auxiliares).
- `figures/` : carpeta para todas las figuras generadas (en la raíz del proyecto).
- `results/` : salida en formato serializado (npz, json) de los experimentos.

Requisitos (sistema y paquetes)
- Python 3.9+ (se ha usado Miniconda en desarrollo).
- Paquetes Python (instalar en un entorno virtual):
