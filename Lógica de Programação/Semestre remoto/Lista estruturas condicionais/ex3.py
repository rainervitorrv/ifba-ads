nota1 = float(input('Informe a 1ª nota: '))
nota2 = float(input('Informe a 2ª nota: '))

media = (nota1 + nota2) / 2


if (media == 10):
    print('Aprovado com Distinção')
elif(media >= 7):
    print('Aprovado')
else:
    print('Reprovado')
