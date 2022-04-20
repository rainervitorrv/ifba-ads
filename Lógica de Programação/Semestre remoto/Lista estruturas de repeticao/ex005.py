while True:
    habitantes_populacao_a = int(
        input('Infome a quantidade de habitantes da população A: ')
    )
    if habitantes_populacao_a > 0:
        while True:
            taxa_anual_crescimento_da_populacao_a = float(
                input('Informe a taxa de crescimento da população A: ')
            )
            if taxa_anual_crescimento_da_populacao_a > 0:
                while True:
                    habitantes_populacao_b = int(
                        input('Infome a quantidade de habitantes da população B: ')
                    )
                    if habitantes_populacao_b > 0:
                        while True:
                            taxa_anual_crescimento_da_populacao_b = float(
                                input(
                                    'Informe a taxa de crescimento da população B: ')
                            )
                            if taxa_anual_crescimento_da_populacao_b > 0:
                                break
                            print('Taxa de crescimento inválida!')
                        break
                    print('Quantidade de habitantes inválida!')
                break
            print('Taxa de crescimento inválida!')
        break
    print('Quantidade de habitantes inválida!')

totalAnos = 0

while habitantes_populacao_a < habitantes_populacao_b:

    totalAnos = totalAnos + 1

    habitantes_populacao_a += habitantes_populacao_a * \
        taxa_anual_crescimento_da_populacao_a

    habitantes_populacao_b += habitantes_populacao_b * \
        taxa_anual_crescimento_da_populacao_b

if habitantes_populacao_b < habitantes_populacao_a:
    print('A quantidade de habitantes da população A é maior que o total de habitantes da população B')
elif habitantes_populacao_a == habitantes_populacao_b:
    print('Em ', totalAnos, ' anos a população A será igual a população B')
else:
    print('Em ', totalAnos, ' anos a população A será maior que a população B')
