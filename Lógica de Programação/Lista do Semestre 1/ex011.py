# O programa calcula o seu peso ideal
# Autor: Rainer Sousa
# Data: 07/04/2020

altura = float(input('Informe a sua altura: '))
sexo = str(input('Qual o seu sexo? \nDigite Masculino ou Femenino: ')).strip().lower()

if(sexo == 'masculino'):
    print('Seu peso ideal seria {}KG'.format((72.7 * altura) - 58))
elif(sexo == 'femenino'):
    print('Seu peso ideal seria {}KG'.format((62.1 * altura)))
else:
    print('O valor do sexo informado não foi encontrado!')