# Calculadora simples
# Desenvolvido por Rainer de Sousa
# https://github.com/rainervitorrv/ifba-ads

numeros = []


def soma(numero1, numero2):
    return float(numero1) + float(numero2)


def subtracao(numero1, numero2):
    return float(numero1) - float(numero2)


def multiplicacao(numero1, numero2):
    return float(numero1) * float(numero2)


def divisao(numero1, numero2):
    if (numero2 <= 0):
        return "O divisor é invalido."
    return numero1 / numero2


def potenciacao(numero):
    return int(numero) * int(numero)


def fatorial(numero):
    fatorial = 1

    i = 2

    while i <= int(numero):
        fatorial = fatorial * i
        i += 1
    return fatorial


while True:

    print('\n- Escolha uma das opções: ')
    print('1 <= Soma')
    print('2 <= Subtração')
    print('3 <= Multiplicação')
    print('4 <= Divisão')
    print('5 <= Potenciação')
    print('6 <= Fatorial')
    print('0 <= Sair')

    opcao = int(input('\n>>> '))

    if opcao == 1:
        print('Informe o 1° número: ')
        numero1 = input('\n> ')
        print('Informe o 2° número: ')
        numero2 = input('\n> ')

        print('---------------------------------')
        print('---------------------------------')
        print('\nA soma dos números é ', soma(numero1, numero2))
        print('---------------------------------\n')

    elif opcao == 2:
        print('Informe o 1° número: ')
        numero1 = input('\n> ')
        print('Informe o 2° número: ')
        numero2 = input('\n> ')

        print('---------------------------------')
        print('---------------------------------')
        print('\nA subtração dos números é ', subtracao(numero1, numero2))
        print('---------------------------------\n')

    elif opcao == 3:
        print('Informe o 1° número: ')
        numero1 = input('\n> ')
        print('Informe o 2° número: ')
        numero2 = input('\n> ')

        print('---------------------------------')
        print('---------------------------------')
        print('\nA multiplicação dos números é ',
              multiplicacao(numero1, numero2))
        print('---------------------------------\n')

    elif opcao == 4:
        print('Informe o 1° número: ')
        numero1 = float(input('\n> '))
        print('Informe o 2° número: ')
        numero2 = float(input('\n> '))

        print('---------------------------------')
        print('---------------------------------')
        print(f'\nO resultado é {divisao(numero1, numero2)}')
        print('---------------------------------\n')

    elif opcao == 5:
        print('Informe o número: ')
        numero = input('\n>')

        print('---------------------------------')
        print('---------------------------------')
        print('\nA potencia de {} é {}'.format(numero, potenciacao(numero)))
        print('---------------------------------\n')
    elif opcao == 6:
        print('Informe o número: ')
        numero = input('\n>')

        print('---------------------------------')
        print('---------------------------------')
        print('\nA Fatoria de {} é {}'.format(numero, fatorial(numero)))
        print('---------------------------------\n')
    elif opcao == 0:
        break
    else:
        print('\nOpção inválida! \nDigite uma nova opção.')
