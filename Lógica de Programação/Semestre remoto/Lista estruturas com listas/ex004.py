A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0
somaQuadrado = 0

while i < len(A):
    A[i] *= A[i]
    somaQuadrado += A[i]
    i += 1

print(f'A soma do quadrado dos elementos é {somaQuadrado}')
