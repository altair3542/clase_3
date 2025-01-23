# Ejercicio 4: Ordenar Lista de Palabras Alfabéticamente (Insertion Sort)
# Instrucciones:

# Solicita al usuario que ingrese 5 palabras separadas por espacios.
# Ordena las palabras en orden alfabético utilizando el método de inserción.
# Muestra la lista ordenada.
palabras = input("Ingrese 5 palabras separadas por espacio: ").split()

for i in range(1, len(palabras)):
    clave = palabras[i]
    j = i - 1
    while j >= 0 and clave < palabras[j]:
        palabras[j+1] = palabras[j]
        j -= 1
    palabras[j+1] = clave

print(f"palabras ordenadas alfabeticamente: {palabras}. ")
