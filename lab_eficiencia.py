# Complejidad temporal: O(n^2) peor y promedio, O(n) mejor caso
# Complejidad espacial: O(1) - ordena en el mismo arreglo
def ordenamiento_burbuja(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# Complejidad temporal: O(n log n) en todos los casos
# Complejidad espacial: O(n) - necesita arreglos auxiliares
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mitad = len(arr) // 2
    izq = merge_sort(arr[:mitad])
    der = merge_sort(arr[mitad:])
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i]); i += 1
        else:
            resultado.append(der[j]); j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

# Complejidad temporal: O(n) peor y promedio, O(1) mejor caso
# Complejidad espacial: O(1)
def busqueda_lineal(arr, objetivo):
    for i, valor in enumerate(arr):
        if valor == objetivo:
            return i
    return -1

# Complejidad temporal: O(log n)
# Complejidad espacial: O(1)
# Requisito: el arreglo debe estar ordenado
def busqueda_binaria(arr, objetivo):
    inicio, fin = 0, len(arr) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1