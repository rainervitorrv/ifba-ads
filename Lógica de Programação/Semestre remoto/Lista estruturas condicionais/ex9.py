salarioColaborador = float(input('Informe o seu sálario: '))

if salarioColaborador <= 280:
    salarioReajustado = salarioColaborador + (salarioColaborador * 0.2)
    print('SALARIO: R$ {:.2f} (REAJUSTADO EM 20%)'.format(salarioReajustado))
elif salarioColaborador <= 700:
    salarioReajustado = salarioColaborador + (salarioColaborador * 0.15)
    print('SALARIO: R$ {:.2f} (REAJUSTADO EM 15%)'.format(salarioReajustado))
elif salarioColaborador <= 1500:
    salarioReajustado = salarioColaborador + (salarioColaborador * 0.1)
    print('SALARIO: R$ {:.2f} (REAJUSTADO EM 10%)'.format(salarioReajustado))
else:
    salarioReajustado = salarioColaborador + (salarioColaborador * 0.05)
    print('SALARIO ANTERIOR AO REAJUSTE R$ {:.2f}'.format(salarioColaborador))
    print('PERCENTUAL DE AUMENTO: 5%')
    print('VALOR DO AUMENTO: R$ {:.2f}'.format(salarioColaborador * 0.05))
    print('NOVO SALARIO: R$ {:.2f} (REAJUSTADO EM 5%)'.format(
        salarioReajustado))
