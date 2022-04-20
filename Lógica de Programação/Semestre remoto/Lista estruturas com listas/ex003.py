pessoas = []

for i in range(1, 6):
    dados = []
    print(f'PESSOA {i}')
    dados.append(f'Pessoa {i}')
    dados.append(
        int(input(f'Informe a idade da {i}ª pessoa : '))
    )
    dados.append(
        float(input(f'Informe a altura da {i}ª pessoa: '))
    )

    pessoas.append(dados)
    print('\n')

pessoas.reverse()

for pessoa in pessoas:
    print(f'>>> Pessoa {pessoa[0]}')
    print(f'Idade: {pessoa[1]}')
    print(f'Altura: {pessoa[2]}')
