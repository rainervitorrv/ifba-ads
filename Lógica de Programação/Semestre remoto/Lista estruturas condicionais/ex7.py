numeros = []

numeros.append(float(input('Informe o 1º número: ')))
numeros.append(float(input('Informe o 2º número: ')))
numeros.append(float(input('Informe o 3º número: ')))

numeros.sort(reverse=True)

print('A ordem decrescente é ', numeros)
