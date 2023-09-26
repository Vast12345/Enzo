# de lanzar un dado 100 veces, imprimir cuntas veces cae la cara 5

import random

cae5 = 0 # variable de tipo contador
for i in range(100):
    dado = random.randrange(1, 7)
    if dado == 5:
        cae5 += 1

print(f"The side 5 fell {cae5} times")