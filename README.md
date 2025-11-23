# Proyecto: Análisis de Optimización

Descripción
-----------
Este repositorio contiene el análisis teórico y experimental de la función

      f(x, y) = log(x^2 + y^2 + 1) * arctan(x^2 + y^2)

Se incluyen implementaciones y comparaciones de varios algoritmos de optimización (gradiente con paso fijo y adaptativo, método de Newton, un esquema híbrido, entre otros), además de experimentación masiva para estudiar la robustez y convergencia desde múltiples puntos iniciales.

Estructura del repositorio
--------------------------
- `notebooks/optimization_analysis.ipynb` : Notebook principal que contiene
   - definiciones de la función, gradiente y Hessiana,
   - implementaciones de los algoritmos usados,
   - experimentos reproducibles y visualizaciones.
- `Report/` : fuentes LaTeX y artefactos del informe (`optimization_report.tex`, `.aux`, PDF generado).
- `figures/` : figuras generadas por el notebook (plots 3D, contornos, trayectorias, análisis estadístico).
- `notebooks/` : notebooks auxiliares (si los hubiera) y material para análisis reproducible.

Requisitos
----------
- Python 3.9 o superior (se recomienda usar un entorno virtual con Conda o venv).
- Paquetes Python (puedes instalarlos en un entorno virtual):

```bash
python -m pip install -r requirements.txt
```

Ejemplo de `requirements.txt` recomendado:

```
numpy
matplotlib
seaborn
scipy
jupyter
nbconvert
```

Uso y reproducción
------------------
1. Crear y activar un entorno virtual (Conda):

```powershell
conda create -n optim_env python=3.10 -y
conda activate optim_env
python -m pip install -r requirements.txt
```

2. Ejecutar el notebook interactivamente (recomendado):

```powershell
jupyter lab notebooks/optimization_analysis.ipynb
# o
jupyter notebook notebooks/optimization_analysis.ipynb
```

3. Para ejecutar el notebook de forma no interactiva y guardar la salida:

```powershell
jupyter nbconvert --to notebook --execute "notebooks/optimization_analysis.ipynb" --output executed_notebook.ipynb


Resultados y figuras
--------------------
Las figuras generadas por el Notebook se guardan en `figures/`. El informe en `Report/` resume los hallazgos teóricos y experimentales.
