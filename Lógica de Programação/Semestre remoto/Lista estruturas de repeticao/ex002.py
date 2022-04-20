usuario = str(input('Informe seu usuário: ')).strip()

while True:
    senha = str(input('Informe a sua senha: '))
    if senha.strip() != usuario:
        break
    print('Senha inválida! Usuário e senha não podem ser iguais.')
