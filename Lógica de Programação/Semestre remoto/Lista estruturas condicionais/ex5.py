numero1 = float(input('Informe o 1º número: '))
numero2 = float(input('Informe o 2º número: '))
numero3 = float(input('Informe o 3º número: '))

if (numero1 < numero2 and numero1 < numero3):
    print('O menor número é ', numero1)
elif (numero2 < numero3):
    print('O menor número é ', numero2)
else:
    print('O menor número é ', numero3)
