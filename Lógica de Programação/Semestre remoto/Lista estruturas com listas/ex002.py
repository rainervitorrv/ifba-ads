numerosInteiros = [1, 2, 3, 4, 5]

soma = 0
multiplicacao = 1
contador = 0

print('Os números foram ', end='')

for numero in numerosInteiros:
    contador += 1
    soma += numero
    multiplicacao *= numero
    print(numero, end='')
    if contador == len(numerosInteiros) - 1:
        print(' e ', end='')
    elif contador < len(numerosInteiros):
        print(', ', end='')
    else:
        print('.')


print(f'A soma dos números é {soma}.')
print(f'A multiplicação dos números é {multiplicacao}.')
