numero = []
soma = 0
media = 0

for i in range(5):
    numero.append(float(input('Infome o {}º número: '.format(i+1))))
    soma += numero[i]

media = soma / 5
print('A soma dos números é ', soma)
print('A média dos números é ', media)
