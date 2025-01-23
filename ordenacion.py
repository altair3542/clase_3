#Complejidad algoritmica y metodos de ordenación.
#(Bubble Sort e insertion sort)

#cuando trabajamos con algoritmos, es fundamental evaluar que tan eficientes son en terminos de ejecucion y uso de memoria. Esta eficiencia se mide mediante la complejidad algoritmica. esto nos ayuda estimar el comportamiendo del algoritmo cuando el tamaño de los datos crece.


#la complejidad algoritmica mide los recursos que necesita un algoritmo para ejecutarse. y se mide en terminos de:

#tiempo de ejecución (complejidad temporal:)
#cuanto tiempo toma ejecutar el algoritmo en funcion de la cantidad de los datos en entrada (n), se suele expresar en big O O(n), O(n2), O(log n).

#uso de memoria o complejidad espacial):
#Cuanta memoria adicional requiere el algoritmo para ejecutarse.
#tambien se expresa en Big O

#Notación Big O
# describir como crece el tiempo de ejecucion de un algoritmo en relacion a su tamaño de entrada. algunos de los ordenes de complejidad mas comunes son:

#Como ordenar...

#es el proceso de organizar elementos en un orden especifico (asecendente y descendente.) Existen multimples algorimos de ordenacion, cada uno con sus ventajas y sus desventajas. sobretodo en terminos de eficiencia.

#Ordenacion por burbuja o bubble sort.
# este algoritmo compara elementos adyacentes y los intercambia si estan en orden incorrecto, esto se repite hasta que no se necesiten mas intercambios.

#en el mejor de los casos es lineal. en el peor, cuadratico y espacialmente hablando es constante.

numeros = [5, 3, 8, 4, 2]
n = len(numeros)

for i in range(n-1):
    for j in range(n - 1 - i):
        if numeros[j] > numeros[j+1]:
            temp = numeros[j]
            numeros[j] = numeros[j+1]
            numeros[j+1] = temp

print(f"lista ordenada con bubble sort: {numeros}")

#ventajas
#facil de entender e implementar
#funciona bien con listas pequeñas.

#desventajas
# ineficiente para listas grandes
# realiza muchas comparaciones que son innecesarias


# Metodo de ordenacion por inserción

# construye la lista ordenada de manera incremental, insertando cada elemento en la posicion correcta respecto a los ya ordenados.

# en el mejor de los casos es de complejidad lineal
# en el peor de los casos es cuadratico
#espacialmente hablando es constante.


# [7, 3, 5, 2, 6]
#  → [3, 7, 5, 2, 6]
#  → [3, 5, 7, 2, 6]
#  → [2, 3, 5, 7, 6]

num = [7, 3, 5, 2, 6]
n = len(num)

for i in range(1, n):
    clave = num[i]
    j = i -1
    while j >= 0 and num[j] > clave:
        num[j + 1] = num[j]
        j -= 1
    num[j + 1] = clave

print(f"lista ordenada con insertion: {num}")
