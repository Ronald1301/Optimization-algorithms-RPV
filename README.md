 # Proyecto: Análisis de Optimización

Este repositorio contiene notebooks, scripts y recursos para el análisis numérico de la función
f(x,y) = log(x^2 + y^2 + 1) * arctan(x^2 + y^2) y experimentación con distintos algoritmos de
optimización (Gradiente, Newton, Quasi-Newton, Trust-Region, métodos de penalidad, etc.).

Contenido principal
- `notebooks/optimization_analysis.ipynb` : notebook principal con definiciones, análisis teórico,
   implementaciones y experimentos reproducibles.
- `notebooks/optimization_extras.ipynb` : implementaciones adicionales (BFGS, DFP, región de confianza,
   penalidad, visualizaciones avanzadas y experimentos extendidos).
- `Report/` : archivos relacionados con el informe LaTeX (`optimization_report.tex`, auxiliares).
- `figures/` : carpeta para todas las figuras generadas (en la raíz del proyecto).
- `results/` : salida en formato serializado (npz, json) de los experimentos.

Requisitos (sistema y paquetes)
- Python 3.9+ (se ha usado Miniconda en desarrollo).
- Paquetes Python (instalar en un entorno virtual):

```powershell
python -m pip install -r requirements.txt
# o, si no existe requirements.txt
python -m pip install numpy scipy matplotlib seaborn numba pandas sympy
```

Atajos y ejecución (PowerShell)
- Abrir el notebook en VS Code o JupyterLab y seleccionar el kernel correcto (p. ej. el intérprete de
   Miniconda).
- Para regenerar las figuras que incluye el informe (si existe `Report/generate_figures.py`):

```powershell
& 'C:\Users\TIGER\Miniconda3\python.exe' 'c:\PRO\TE Optimizacion\Report\generate_figures.py'
```

- Para ejecutar los experimentos desde un script (si existe `experiments/run_experiments.py`):

```powershell
& 'C:\Users\TIGER\Miniconda3\python.exe' 'c:\PRO\TE Optimizacion\experiments\run_experiments.py'
```

Dónde se guardan las figuras
- Todas las figuras generadas por los notebooks se guardan en `figures/` en la raíz del proyecto,
   por ejemplo `c:\PRO\TE Optimizacion\figures\function_3d_20251113-110250.png`.
- El helper `save_fig(name, ext='png', ...)` (definido en los notebooks) detecta si ya existe un
   fichero con patrón `{name}_*.{ext}` y, por defecto, evita sobrescribir o duplicar la imagen.

Buenas prácticas para el entregable
- Incluir en el PDF (LaTeX) un enlace al repositorio GitHub con el código y las instrucciones para
   reproducir los experimentos.
- Comprimir solo los archivos necesarios para revisión: `notebooks/`, `figures/`, `results/`, `Report/` y
   `README.md`.

Notas sobre reproducibilidad y límites
- Se recomienda ejecutar experimentos de prueba primero con pocos puntos iniciales y mallas pequeñas
   antes de usar rangos grandes como [-100,100] para evitar overflow o tiempos largos.
- Si quieres centralizar utilidades (por ejemplo `save_fig`) en un módulo `scripts/io_utils.py`,
   puedo crear ese archivo e importar la función desde ambos notebooks para mantener comportamiento
   consistente.

Contacto y enlace GitHub
- Si quieres que publique esto en un repositorio público o privado, dime el nombre y lo subo con un
   `README.md` y una rama inicial. Actualmente el repositorio local puede subirse con:

```powershell
git init
git add .
git commit -m "Initial commit: análisis de optimización"
```

---
Archivo actualizado automáticamente: `save_fig` ahora evita duplicados por nombre.
