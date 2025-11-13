Proyecto: Análisis de Optimización

Instrucciones rápidas:

1) Seleccionar kernel recomendado en VS Code
   - Recomendado: Python Miniconda instalado en C:\Users\TIGER\Miniconda3\python.exe
   - Opcional: registrar kernel con ipykernel:
     & 'C:\Users\TIGER\Miniconda3\python.exe' -m pip install ipykernel
     & 'C:\Users\TIGER\Miniconda3\python.exe' -m ipykernel install --user --name python3_miniconda --display-name "Python 3.13 (Miniconda)"

2) Generar figuras usadas en el informe (recomendado antes de compilar LaTeX):
   & 'C:\Users\TIGER\Miniconda3\python.exe' 'c:\PRO\TE Optimizacion\Report\generate_figures.py'
   Esto generará `Report/placeholder_robustez.png` y `figures/robustez_example.png`.

3) Ejecutar los experimentos rápidos y almacenar resultados/figuras:
   & 'C:\Users\TIGER\Miniconda3\python.exe' 'c:\PRO\TE Optimizacion\experiments\run_experiments.py'
   Esto creará `results/summary.json` y `figures/example_distance_iters.png`.

Archivos creados por el asistente (si no existían):
- `src/optimization.py` : definiciones y algoritmos (f, grad_f, hess_f, GD, Newton, híbrido)
- `experiments/run_experiments.py` : script para ejecutar experimentos rápidos
- `Report/generate_figures.py` : genera `Report/placeholder_robustez.png` y copia ejemplo a `figures/`
- `results/` : directorio para resultados JSON
- `figures/` : directorio para figuras generadas

Si prefieres que ejecute los scripts ahora (generar figuras / correr experimentos) dímelo y lo ejecuto con el intérprete Miniconda que ya tienes configurado.
