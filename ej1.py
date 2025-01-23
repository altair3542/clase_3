# Ejercicio 1: Ordenar una Lista de Números Ingresados por el Usuario (Bubble Sort)
# Instrucciones:

# Solicita al usuario que ingrese 6 números separados por espacios.
# Usa el método de ordenación burbuja para organizarlos de menor a mayor.
# Muestra la lista ordenada.

numeros = input("ingrese 6 numeros separados por espacios: ").split()

for i in range(len(numeros)):
    numeros[i] = int(numeros[i])

n = len(numeros)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1],numeros[j]

print(f"La lista ordenada es: {numeros}")
