import random
import time
# pyrefly: ignore[missing-import]
from lab_eficiencia import ordenamiento_burbuja, merge_sort, busqueda_lineal, busqueda_binaria

def medir(funcion, datos):
    inicio = time.perf_counter()
    funcion(datos[:])
    fin = time.perf_counter()
    return fin - inicio

def medir_busqueda(funcion, datos, objetivo):
    inicio = time.perf_counter()
    funcion(datos, objetivo)
    fin = time.perf_counter()
    return fin - inicio

def main():
    tamanos = [1000, 2000, 4000, 8000]
    print("=== ORDENAMIENTO ===")
    for nombre, funcion in [("Burbuja", ordenamiento_burbuja), ("Merge Sort", merge_sort)]:
        print(f"\n{nombre}")
        print(f"{'n':<8} {'Tiempo (s)':<15} {'Razon':<10}")
        tiempo_anterior = None
        for n in tamanos:
            datos = [random.randint(0, 100000) for _ in range(n)]
            tiempo = medir(funcion, datos)
            razon = tiempo / tiempo_anterior if tiempo_anterior else 0
            print(f"{n:<8} {tiempo:<15.6f} {razon:<10.2f}")
            tiempo_anterior = tiempo

    print("\n=== BUSQUEDA ===")
    for nombre, funcion, ordenada in [("Lineal", busqueda_lineal, False), ("Binaria", busqueda_binaria, True)]:
        print(f"\n{nombre}")
        print(f"{'n':<8} {'Tiempo (s)':<15} {'Razon':<10}")
        tiempo_anterior = None
        for n in tamanos:
            datos = [random.randint(0, 100000) for _ in range(n)]
            if ordenada:
                datos = sorted(datos)
            objetivo = datos[n // 2]
            tiempo = medir_busqueda(funcion, datos, objetivo)
            razon = tiempo / tiempo_anterior if tiempo_anterior and tiempo_anterior > 0 else 0
            print(f"{n:<8} {tiempo:<15.6f} {razon:<10.2f}")
            tiempo_anterior = tiempo if tiempo > 0 else tiempo_anterior

if __name__ == "__main__":
    main()