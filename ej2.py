# Ejercicio 2: Ordenar Lista de Productos por Precio (Insertion Sort)
# Instrucciones:

# Pide al usuario ingresar los precios de 5 productos separados por espacios.
# Usa el método de inserción para ordenarlos de menor a mayor.
# Muestra la lista ordenada.
precios = input("Ingrese los precios de 5 productos separados por espacio: ").split()

for i in range(len(precios)):
    precios[i] = float(precios[i])

for i in range(1, len(precios)):
    clave = precios[i]
    j = i - 1
    while j >= 0 and clave < precios[j]:
        precios[j + 1] = precios[j]
        j -= 1
    precios[j + 1] = clave

print(f"Precios ordenados: {precios}")
