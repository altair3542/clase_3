import random, time

start_creation_time = time.time()
size = 300000000
array = [random.randint(1, 1500000000) for _ in range(size)]
end_creation_time = time.time()
random_index = random.randint(0, size - 1)

start_time = time.time()
value = array[random_index]
end_time = time.time()

print(f"el tiempo de acceso fue de {end_creation_time - start_creation_time: .10f} segundos")

print(f"Ele elemento en el indice {random_index} es {value}")
print(f"el tiempo de acceso fue de {end_time - start_time: .10f} segundos")
