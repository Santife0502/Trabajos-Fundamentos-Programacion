#programa para resolver un sistema de ecuaciones 

#como ejemplo tenemos el siguiente sistema
#2x + 3y = 13
#x - y = -1

import numpy as np

# Definir la matriz de coeficientes
A = np.array([[2, 3], [1, -1]])

# Definir el vector de términos independientes
B = np.array([13, -1])

# Resolucion del sistema de ecuaciones
X = np.linalg.solve(A, B)

# Solucion del sistema
print("La solución del sistema de ecuaciones es:")
print(f"x = {X[0]}, y = {X[1]}")