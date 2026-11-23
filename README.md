# Lab Eficiencia - 4
## Algoritmos de Ordenamiento y Busqueda

Autora: Shirley Armijos
Repositorio: Shirley_Armijos_lab_eficiencia-4

### Descripcion
Este proyecto implementa y compara la eficiencia de algoritmos de ordenamiento y busqueda en Python, midiendo el tiempo de ejecucion con diferentes tamanos de datos.

### Archivos
- `lab_eficiencia.py`: Contiene los algoritmos bubble_sort, merge_sort, quick_sort, busqueda_lineal y busqueda_binaria, ademas de la funcion generar_datos.
- `main.py`: Ejecuta las pruebas, mide los tiempos con time.time() y muestra los resultados.

### Algoritmos implementados
- Bubble Sort - O(n^2)
- Merge Sort - O(n log n)
- Quick Sort - O(n log n) en promedio, O(n^2) en peor caso
- Busqueda Lineal - O(n)
- Busqueda Binaria - O(log n)

### Como ejecutar
1. Clonar el repositorio o descargar los archivos
2. Ejecutar en la terminal:
python main.py

### Resultados esperados
- Bubble Sort es el mas lento con datos grandes.
- Merge Sort y Quick Sort son mucho mas rapidos.
- La busqueda binaria es mucho mas rapida que la lineal en listas ordenadas, porque solo hace alrededor de 20 comparaciones para 1 millon de datos, mientras la lineal puede hacer hasta 1 millon.

### Conclusion
La eleccion del algoritmo afecta mucho el tiempo de ejecucion. Para datos grandes conviene usar Merge Sort o Quick Sort y busqueda binaria en listas ordenadas.
