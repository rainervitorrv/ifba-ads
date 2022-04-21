# Gerenciamento de alunos

alunos = [['RAINER', '12313', 'ads']]


def adicionarAluno(nome, cpf, curso):
    dadosAluno = [nome.upper(), cpf, curso]
    alunos.append(dadosAluno)


def pesquisarAluno(nome):
    return [alunos.index(aluno) for aluno in alunos if nome in aluno]


def editarAluno(posicao, nome, cpf, curso):
    alunos[posicao] = [nome, cpf, curso]


def excluirAluno(posicao):
    del alunos[posicao]


print('+++ Gerenciamento de Alunos v1.0.0')

opcao = 1

while opcao != 0:

    print('\n- Escolha uma das opções: ')
    print('1 <= Cadastrar Aluno')
    print('2 <= Buscar Aluno')
    print('3 <= Editar Aluno')
    print('4 <= Apagar registro de Aluno')
    print('5 <= Ver todos alunos')
    print('0 <= Sair')

    opcao = int(input('\n>>> '))

    if opcao == 1:
        print('Informe o nome do aluno: ')
        nome = str(input('\n> '))
        print('Informe o CPF: ')
        cpf = str(input('\n> '))
        print('Informe o curso: ')
        curso = str(input('\n> '))

        adicionarAluno(nome, cpf, curso)

        print('\n+ Cadastro realizado com sucesso!')

    elif opcao == 2:
        print('\nDigite o nome do aluno para busca: ')
        busca = str(input('\n> '))
        registro = pesquisarAluno(busca.upper())

        if (registro):
            registro = registro[0]
            print('\nRegistro encontrado...')
            print('Nome: ', alunos[registro][0])
            print('CPF: ', alunos[registro][1])
            print('Curso: ', alunos[registro][2])
        else:
            print('\nNenhum registro foi encontrado!')

    elif opcao == 3:
        print('\nDigite o nome do aluno para edição: ')
        busca = str(input('\n> '))
        registro = pesquisarAluno(busca.upper())
        if (registro):
            registro = registro[0]
            print('Registro encontrado!')
            print('Insira abaixo as novas informações: ')
            print('\nNome: ')
            nome = str(input('\n> '))
            print('CPF: ')
            cpf = str(input('\n> '))
            print('Curso: ')
            curso = str(input('\n> '))

            editarAluno(registro, nome.upper(), cpf, curso)

            print('\n+ Registro atualizado com sucesso!')

        else:
            print('Nenhum aluno encontrado')

    elif opcao == 4:
        print('\nDigite o nome do aluno para deletar: ')
        busca = str(input('\n> '))
        registro = pesquisarAluno(busca.upper())
        if (registro):
            registro = registro[0]
            excluirAluno(registro)
            print('\n+ Registro apagado com sucesso!')

        else:
            print('Nenhum aluno encontrado')
    elif opcao == 5:
        for aluno in alunos:
            print('-------------------------')
            print('\nNome: ', aluno[0])
            print('\nCPF: ', aluno[1])
            print('Curso: ', aluno[2])
            print('\n')
    elif opcao == 0:
        break
    else:
        print('Opção inválida! \nDigite uma nova opção.')

    input('\nPressione ENTER para continuar...')
