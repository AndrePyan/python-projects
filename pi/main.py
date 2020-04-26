# Estimar pi
import random
import msvcrt
n = int(input("dijite un numero: "))
def estimar_pi(n):
    punto_circulo = 0
    punto_total = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1
            punto_circulo += 1
        punto_total += 1
    return 4 * num_punto_circulo/num_punto_total